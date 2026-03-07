from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

from src.ai.analyzer import ContentAnalyzer
from src.ai.client import OpenAIClient
from src.models import AIConfig, AIProvider, ContentItem, SourceType


class FakeAIClient:
    def __init__(self, response: str):
        self.response = response

    async def complete(
        self,
        system: str,
        user: str,
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ) -> str:
        return self.response


def make_item() -> ContentItem:
    return ContentItem(
        id="telegram:test:1",
        source_type=SourceType.TELEGRAM,
        title="Structured output regression",
        url="https://example.com/post",
        content="This is a test item.",
        author="tester",
        published_at=datetime.now(timezone.utc),
    )


def test_openai_client_extracts_structured_message_content(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    config = AIConfig(provider=AIProvider.OPENAI, model="deepseek-chat", api_key_env="OPENAI_API_KEY")
    client = OpenAIClient(config)

    class FakeCompletions:
        async def create(self, **kwargs):  # type: ignore[no-untyped-def]
            return SimpleNamespace(
                choices=[
                    SimpleNamespace(
                        message=SimpleNamespace(
                            content=[
                                {"type": "text", "text": '{"score": 9, "reason": "high impact"}'},
                            ]
                        )
                    )
                ]
            )

    client.client = SimpleNamespace(chat=SimpleNamespace(completions=FakeCompletions()))

    result = asyncio.run(client.complete(system="sys", user="usr"))

    assert result == '{"score": 9, "reason": "high impact"}'


def test_content_analyzer_parses_wrapped_json_response() -> None:
    analyzer = ContentAnalyzer(
        FakeAIClient(
            """
            <think>hidden reasoning</think>
            Here is the result:
            ```json
            {
              "score": "8/10",
              "reason": "Useful technical update.",
              "summary": "A concise summary.",
              "tags": "ai, tooling, mcp"
            }
            ```
            """
        )
    )
    item = make_item()

    analyzed = asyncio.run(analyzer.analyze_batch([item]))

    assert analyzed[0].ai_score == 8.0
    assert analyzed[0].ai_reason == "Useful technical update."
    assert analyzed[0].ai_summary == "A concise summary."
    assert analyzed[0].ai_tags == ["ai", "tooling", "mcp"]
