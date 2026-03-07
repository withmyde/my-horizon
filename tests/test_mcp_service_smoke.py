from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace

from src.mcp.server import hz_get_metrics
from src.mcp.service import HorizonPipelineService


def test_validate_config_smoke(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    config_path = tmp_path / "config.json"
    config_path.write_text(
        (repo_root / "data" / "config.example.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    result = asyncio.run(
        service.validate_config(
            horizon_path=str(repo_root),
            config_path=str(config_path),
            check_env=False,
        )
    )

    assert result["config_path"] == str(config_path.resolve())
    assert result["enabled_sources"]
    assert result["missing_env"] == []


def test_get_effective_config_can_filter_sources(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    config_path = tmp_path / "config.json"
    config_path.write_text(
        (repo_root / "data" / "config.example.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    result = service.get_effective_config(
        horizon_path=str(repo_root),
        config_path=str(config_path),
        sources=["rss"],
    )

    assert result["selected_sources"] == ["rss"]
    assert result["config"]["sources"]["github"] == []
    assert result["config"]["sources"]["rss"]


def test_metrics_tool_smoke() -> None:
    result = hz_get_metrics()

    assert result["ok"] is True
    assert result["tool"] == "hz_get_metrics"


def test_enrich_items_returns_noop_for_empty_stage(tmp_path: Path, monkeypatch) -> None:
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    service.run_store.create_run("run-empty")

    monkeypatch.setattr(service, "_load_stage_items", lambda **kwargs: ([], SimpleNamespace()))

    result = asyncio.run(service.enrich_items(run_id="run-empty"))

    assert result["run_id"] == "run-empty"
    assert result["enriched"] == 0
    assert result["citation_count"] == 0
    assert result["skipped"] is True
    assert result["reason"] == "empty_input"
    assert service.run_store.load_items("run-empty", "enriched") == []
    assert service.run_store.load_meta("run-empty")["enrich_skipped"] is True


def test_run_pipeline_skips_enrich_when_filter_is_empty(tmp_path: Path, monkeypatch) -> None:
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    service.run_store.create_run("run-empty-filter")

    async def fake_fetch_items(**kwargs):  # type: ignore[no-untyped-def]
        return {"run_id": "run-empty-filter", "meta": {"raw_count": 3}}

    async def fake_score_items(**kwargs):  # type: ignore[no-untyped-def]
        return {"run_id": "run-empty-filter", "scored": 3}

    async def fake_filter_items(**kwargs):  # type: ignore[no-untyped-def]
        return {"run_id": "run-empty-filter", "kept": 0}

    async def fail_if_called(**kwargs):  # type: ignore[no-untyped-def]
        raise AssertionError("enrich_items should not be called when filtered output is empty")

    async def fake_generate_summary(**kwargs):  # type: ignore[no-untyped-def]
        return {
            "run_id": "run-empty-filter",
            "language": kwargs["language"],
            "source_stage": kwargs["source_stage"],
            "summary_path": "summary.md",
        }

    monkeypatch.setattr(service, "fetch_items", fake_fetch_items)
    monkeypatch.setattr(service, "score_items", fake_score_items)
    monkeypatch.setattr(service, "filter_items", fake_filter_items)
    monkeypatch.setattr(service, "enrich_items", fail_if_called)
    monkeypatch.setattr(service, "generate_summary", fake_generate_summary)
    monkeypatch.setattr(
        service,
        "_build_context",
        lambda **kwargs: (
            SimpleNamespace(config=SimpleNamespace(ai=SimpleNamespace(languages=["zh"]))),
            [],
            [],
        ),
    )

    result = asyncio.run(service.run_pipeline(hours=6, enrich=True))

    assert result["run_id"] == "run-empty-filter"
    assert result["enrich"]["skipped"] is True
    assert result["enrich"]["reason"] == "empty_filtered_stage"
    assert result["summaries"][0]["source_stage"] == "filtered"
