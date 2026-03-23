import json

import pyarrow.parquet as pq

from src.results import ResultsCollector, RunResult


def test_collector_saves_parquet(tmp_path):
    collector = ResultsCollector(str(tmp_path))
    collector.add(RunResult(seed=42, method="a", metrics={"loss": 0.5}))
    collector.add(RunResult(seed=42, method="b", metrics={"loss": 0.3}))
    collector.save_parquet()

    parquet_path = tmp_path / "metrics.parquet"
    assert parquet_path.exists()
    table = pq.read_table(parquet_path)
    assert table.num_rows == 2
    assert "seed" in table.column_names
    assert "method" in table.column_names
    assert "loss" in table.column_names


def test_collector_saves_summary(tmp_path):
    collector = ResultsCollector(str(tmp_path))
    collector.add(RunResult(seed=42, method="a", metrics={"loss": 0.5}))
    collector.add(RunResult(seed=43, method="a", metrics={"loss": 0.3}))
    collector.save_summary()

    summary_path = tmp_path / "summary.json"
    assert summary_path.exists()
    summary = json.loads(summary_path.read_text())
    assert "a" in summary
    assert summary["a"]["loss"]["mean"] == 0.4
    assert summary["a"]["loss"]["n"] == 2
