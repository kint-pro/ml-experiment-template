.PHONY: setup run clean results lint test help

PYTHON = uv run python
CONFIG ?= configs/default.yaml

help:
	@echo "Usage:"
	@echo "  make setup     Install dependencies and create .venv"
	@echo "  make run       Run experiment with default config"
	@echo "  make run CONFIG=configs/custom.yaml"
	@echo "  make results   Generate figures from latest results"
	@echo "  make lint      Run ruff linter"
	@echo "  make test      Run tests"
	@echo "  make clean     Remove results and cached files"

setup:
	uv sync --extra dev

run:
	$(PYTHON) -m src.run --config $(CONFIG)

results:
	$(PYTHON) -m src.visualize --config $(CONFIG)

lint:
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/

test:
	uv run pytest

clean:
	rm -rf results/figures/*
	rm -f results/metrics.parquet results/summary.json results/config_used.json
	find . -type d -name __pycache__ -exec rm -rf {} +
