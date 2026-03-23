# EXPERIMENT_NAME

ONE_SENTENCE_DESCRIPTION.

## Quick Start

```bash
git clone REPO_URL
cd EXPERIMENT_NAME
uv sync
make run
```

Results appear in `results/`. Figures in `results/figures/`.

## Background

WHY_THIS_EXPERIMENT_EXISTS. WHAT_QUESTION_IT_ANSWERS. 2-4 SENTENCES.

See [experiment.md](experiment.md) for the full experiment design, metrics, and comparison framework.

## Installation

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
make setup
```

This installs all dependencies including dev tools (ruff, pytest).

## Usage

### Run the experiment

```bash
make run
```

With a custom config:

```bash
make run CONFIG=configs/custom.yaml
```

### Generate figures from results

```bash
make results
```

### Run tests

```bash
make test
```

### Lint

```bash
make lint
```

## Configuration

All parameters are defined in YAML files under `configs/`.

```yaml
experiment:
  name: "EXPERIMENT_NAME"

seed:
  base: 42
  n_runs: 10       # independent runs for statistical validity

data:
  n_train: 1000
  n_val: 200
  n_test: 200

training:
  epochs: 100
  learning_rate: 0.001
  batch_size: 64
```

See [configs/default.yaml](configs/default.yaml) for all options.

## Project Structure

```
├── configs/
│   └── default.yaml        Experiment configuration
├── src/
│   ├── config.py            Config loading and validation
│   ├── seed.py              Deterministic seed management
│   ├── results.py           Results collection (Parquet + JSON)
│   ├── run.py               Experiment entry point
│   └── visualize.py         Plot generation
├── tests/                   Unit tests
├── data/                    Generated or downloaded data
├── results/
│   ├── figures/             Generated plots (PNG + PDF)
│   ├── metrics.parquet      Per-run metrics
│   └── summary.json         Aggregated results (mean, std, min, max)
├── experiment.md            Experiment design document
├── Makefile                 Common commands
└── pyproject.toml           Dependencies (uv-managed)
```

## Reproducibility

- All random seeds are fixed via config and applied to Python, NumPy, and PyTorch
- Each experiment runs N independent seeds (default: 10) with paired comparison
- The exact config used for each run is saved to `results/config_used.json`
- Results are stored as Parquet (metrics) and JSON (summary statistics)
- Dependencies are pinned in `uv.lock`

To reproduce published results:

```bash
uv sync
make run CONFIG=configs/default.yaml
```

## Results

DESCRIBE_OR_LINK_TO_RESULTS_AFTER_RUNNING.

Summary statistics are in `results/summary.json`. Per-run metrics in `results/metrics.parquet`.

## Citation

```bibtex
@software{EXPERIMENT_NAME,
  author       = {kint},
  title        = {EXPERIMENT_TITLE},
  year         = {2026},
  url          = {REPO_URL},
  license      = {Apache-2.0}
}
```

## License

[Apache 2.0](LICENSE)
