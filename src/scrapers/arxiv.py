"""ArXiv paper scraper implementation using RSS feeds.

This module fetches the latest AI/ML papers from arXiv's RSS feeds,
with deduplication to ensure no paper is sent twice.
"""

import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional
from email.utils import parsedate_to_datetime
import httpx
import feedparser

from .base import BaseScraper
from ..models import ContentItem, SourceType, ArxivConfig

logger = logging.getLogger(__name__)


class ArxivScraper(BaseScraper):
    """Scraper for ArXiv paper RSS feeds."""

    # ArXiv RSS feed base URL for different categories
    ARXIV_RSS_BASE = "http://export.arxiv.org/rss"

    def __init__(
        self,
        config: ArxivConfig,
        http_client: httpx.AsyncClient,
        sent_papers_path: Path,
    ):
        """Initialize ArXiv scraper.

        Args:
            config: ArXiv configuration
            http_client: Shared async HTTP client
            sent_papers_path: Path to the JSON file storing sent paper IDs
        """
        super().__init__({"arxiv": config}, http_client)
        self.config = config
        self.sent_papers_path = sent_papers_path
        self._sent_papers: Optional[set] = None

    @property
    def sent_papers(self) -> set:
        """Load and cache sent papers from file."""
        if self._sent_papers is None:
            if self.sent_papers_path.exists():
                try:
                    with open(self.sent_papers_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        self._sent_papers = set(data.get("sent_ids", []))
                except (json.JSONDecodeError, IOError) as e:
                    logger.warning(f"Failed to load sent papers: {e}")
                    self._sent_papers = set()
            else:
                self._sent_papers = set()
        return self._sent_papers

    def save_sent_papers(self):
        """Save sent papers to file."""
        self.sent_papers_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.sent_papers_path, "w", encoding="utf-8") as f:
            json.dump({"sent_ids": list(self.sent_papers)}, f, indent=2)

    def add_sent_paper(self, paper_id: str):
        """Add a paper ID to the sent list."""
        self.sent_papers.add(paper_id)
        self.save_sent_papers()

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch ArXiv papers from RSS feeds.

        Args:
            since: Only fetch items published after this time (not used for arXiv,
                   we use the sent_papers file for deduplication)

        Returns:
            List[ContentItem]: Fetched ArXiv paper items
        """
        if not self.config.enabled:
            return []

        items = []
        categories = self.config.categories or ["cs.AI"]
        max_results = self.config.max_results or 5

        for category in categories:
            try:
                feed_url = f"{self.ARXIV_RSS_BASE}/{category}"
                category_items = await self._fetch_feed(feed_url, category, max_results)
                items.extend(category_items)
            except Exception as e:
                logger.warning(f"Error fetching ArXiv category {category}: {e}")

        # Sort by published date (newest first) and limit to max_results
        items.sort(key=lambda x: x.published_at or datetime.min, reverse=True)
        items = items[:max_results]

        # Mark fetched papers as sent
        for item in items:
            arxiv_id = self._extract_arxiv_id(item.url)
            if arxiv_id:
                self.add_sent_paper(arxiv_id)

        return items

    async def _fetch_feed(
        self, feed_url: str, category: str, max_results: int
    ) -> List[ContentItem]:
        """Fetch items from a single ArXiv RSS feed.

        Args:
            feed_url: ArXiv RSS feed URL
            category: ArXiv category (e.g., cs.AI)
            max_results: Maximum number of papers to fetch

        Returns:
            List[ContentItem]: ArXiv paper items
        """
        items = []

        try:
            # Fetch feed content with proxy support
            async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
                response = await client.get(feed_url)
                response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)

            for entry in feed.entries[:max_results * 2]:  # Fetch more to filter duplicates
                # Extract arXiv ID from the entry
                entry_id = entry.get("id", "")
                arxiv_id = self._extract_arxiv_id(entry.get("link", entry_id))

                # Skip if already sent
                if arxiv_id in self.sent_papers:
                    logger.debug(f"Skipping already sent paper: {arxiv_id}")
                    continue

                # Parse published date
                published_at = self._parse_date(entry)
                if not published_at:
                    published_at = datetime.now(timezone.utc)

                # Extract content (abstract)
                content = self._extract_content(entry)

                # Extract authors
                authors = []
                if hasattr(entry, "authors"):
                    authors = [author.get("name", str(author)) for author in entry.authors]
                elif hasattr(entry, "author"):
                    authors = [entry.author]

                # Generate PDF URL
                pdf_url = self._generate_pdf_url(arxiv_id)

                item = ContentItem(
                    id=self._generate_id("arxiv", category, arxiv_id),
                    source_type=SourceType.ARXIV,
                    title=entry.get("title", "Untitled").strip(),
                    url=entry.get("link", pdf_url) or pdf_url,
                    content=content,
                    author=", ".join(authors) if authors else "Unknown",
                    published_at=published_at,
                    metadata={
                        "arxiv_id": arxiv_id,
                        "arxiv_category": category,
                        "authors": authors,
                        "pdf_url": pdf_url,
                        "primary_category": self._extract_primary_category(entry),
                        "tags": self._extract_tags(entry),
                    }
                )
                items.append(item)

                if len(items) >= max_results:
                    break

        except httpx.HTTPError as e:
            logger.warning(f"Error fetching ArXiv feed {feed_url}: {e}")
        except Exception as e:
            logger.warning(f"Error parsing ArXiv feed {feed_url}: {e}")

        return items

    def _extract_arxiv_id(self, url_or_id: str) -> str:
        """Extract arXiv ID from URL or ID string.

        Examples:
            - http://arxiv.org/abs/2401.12345v1 -> 2401.12345v1
            - arxiv:2401.12345v1 -> 2401.12345v1
            - 2401.12345 -> 2401.12345
        """
        if not url_or_id:
            return ""

        # Try to extract from URL
        match = re.search(r'arxiv\.org/(?:abs|pdf)/([^/]+)', url_or_id)
        if match:
            return match.group(1)

        # Try to extract from arXiv ID format
        match = re.search(r'(\d{4}\.\d{4,5}(?:v\d+)?)', url_or_id)
        if match:
            return match.group(1)

        return url_or_id.strip()

    def _generate_pdf_url(self, arxiv_id: str) -> str:
        """Generate PDF URL for an arXiv paper."""
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    def _parse_date(self, entry: dict) -> Optional[datetime]:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        from email.utils import parsedate_to_datetime

        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        import calendar
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]),
                            tz=timezone.utc
                        )
                    date_str = entry[field]
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    def _extract_content(self, entry: dict) -> str:
        """Extract abstract/content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Paper abstract
        """
        if "summary" in entry:
            # Clean up HTML tags in summary
            summary = entry.summary
            summary = re.sub(r'<[^>]+>', '', summary)
            return summary.strip()
        elif "description" in entry:
            return entry.description.strip()
        return ""

    def _extract_primary_category(self, entry: dict) -> str:
        """Extract primary category from entry."""
        if hasattr(entry, "primary_category"):
            return entry.primary_category
        elif hasattr(entry, "tags") and entry.tags:
            return entry.tags[0].term if hasattr(entry.tags[0], "term") else str(entry.tags[0])
        return ""

    def _extract_tags(self, entry: dict) -> List[str]:
        """Extract all categories/tags from entry."""
        tags = []
        if hasattr(entry, "tags"):
            for tag in entry.tags:
                if hasattr(tag, "term"):
                    tags.append(tag.term)
                else:
                    tags.append(str(tag))
        return tags
