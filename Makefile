.PHONY: setup run example clean results report lint test help

PYTHON = uv run python
CONFIG ?= configs/default.yaml
BASELINE_DIR ?=

help:
	@echo "Usage:"
	@echo "  make setup                          Install dependencies"
	@echo "  make run                             Run experiment"
	@echo "  make run BASELINE_DIR=path/          Run with diff vs baseline"
	@echo "  make example                         Run example (linear vs ridge vs lasso)"
	@echo "  make results                         Regenerate figures"
	@echo "  make report                          Regenerate report"
	@echo "  make lint                            Run linter"
	@echo "  make test                            Run tests"
	@echo "  make clean                           Remove results"

setup:
	uv sync --group dev

run:
	$(PYTHON) -c "from ml_experiment_stats.cli_run import run_with; from experiment.run import run_single; run_with(run_single)" --config $(CONFIG) $(if $(BASELINE_DIR),--baseline-dir $(BASELINE_DIR))

example:
	$(PYTHON) -c "from ml_experiment_stats.cli_run import run_with; from experiment.example import run_single; run_with(run_single)" --config configs/example.yaml

results:
	$(PYTHON) -c "from ml_experiment_stats.config import load_config; from ml_experiment_stats.visualize import generate_figures; generate_figures(load_config('$(CONFIG)'))"

report:
	uv run mlstats report $(if $(BASELINE_DIR),--baseline-dir $(BASELINE_DIR))

lint:
	uv run ruff check experiment/ tests/
	uv run ruff format --check experiment/ tests/

test:
	uv run pytest

clean:
	rm -rf results/figures/*
	rm -f results/metrics.parquet results/summary.json results/statistics.json
	rm -f results/config_used.json results/report.md results/report.json
	find . -type d -name __pycache__ -exec rm -rf {} +
