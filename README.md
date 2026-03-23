# ML Experiment Template

Reusable template for ML experiments with statistical significance analysis.

## Quick Start

```bash
make setup
make example
```

Results appear in `results/`. Figures in `results/figures/`.

## Installation

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
make setup
```

## Usage

### Implement your experiment

Edit `experiment/run.py` — implement `run_single()`. See `experiment/example.py` for a working demo.

### Run

```bash
make run                                    # run experiment
make run CONFIG=configs/custom.yaml         # custom config
make run BASELINE_DIR=results_baseline/     # with diff vs baseline
```

### CLI (from ml-experiment-stats)

```bash
mlstats summary                             # print results to console
mlstats report                              # generate report.md + report.json
mlstats diff results/ results_baseline/     # compare two result dirs
mlstats check --config configs/default.yaml # CI threshold check
```

### Generate figures from results

```bash
make results
```

## Configuration

All parameters are defined in YAML files under `configs/`.

See [configs/default.yaml](configs/default.yaml) for all options including `statistics` (test type, alpha, correction, ROPE) and `ci` (threshold gating).

## Project Structure

```
experiment/             Your code (modify this)
├── run.py              run_single() — implement this
└── example.py          Working demo (Linear vs Ridge vs Lasso)

configs/                Experiment configs (YAML)
tests/                  Template tests
results/                Output (generated)
```

Statistical engine provided by [ml-experiment-stats](https://github.com/kint-pro/ml-experiment-stats).

## Reproducibility

- All random seeds are fixed via config and applied to Python and NumPy
- Each experiment runs N independent seeds (default: 10) with paired comparison
- The exact config used for each run is saved to `results/config_used.json`
- Results are stored as Parquet (metrics) and JSON (summary statistics)
- Dependencies are pinned in `uv.lock`

## License

[Apache 2.0](LICENSE)
