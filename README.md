# ML Experiment Template

Statistical analysis engine for ML experiments with multi-seed evaluation.

## Quick Start

```bash
make setup
make example
```

Results appear in `results/`. Figures in `results/figures/`.

## Installation

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
make setup          # all dependencies (plots, parquet, bayesian)
```

Install only what you need:

```bash
pip install kint-stats              # core: numpy, scipy, pyyaml
pip install kint-stats[parquet]     # + pyarrow
pip install kint-stats[plots]       # + matplotlib
pip install kint-stats[bayesian]    # + baycomp
pip install kint-stats[all]         # everything
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

### CLI

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
kint_stats/             Installable package (pip install kint-stats)
├── statistics.py       Wilcoxon, t-test, Friedman, Nemenyi, Bayesian, Power
├── report.py           Console + Markdown + JSON renderers
├── diff.py             Baseline comparison
├── ci.py               CI threshold gating
├── results.py          RunResult, ResultsCollector
├── visualize.py        Plots (optional: matplotlib)
├── seed.py             Deterministic seeding (Python, NumPy)
├── config.py           Configuration dataclasses
├── cli.py              mlstats CLI
└── cli_run.py          Experiment orchestration

experiment/             Template (you modify this)
├── run.py              run_single() — implement this
└── example.py          Working demo (Linear vs Ridge vs Lasso)

configs/                Experiment configs (YAML)
tests/                  131 tests
results/                Output (generated)
```

## Reproducibility

- All random seeds are fixed via config and applied to Python and NumPy
- Each experiment runs N independent seeds (default: 10) with paired comparison
- The exact config used for each run is saved to `results/config_used.json`
- Results are stored as Parquet (metrics) and JSON (summary statistics)
- Dependencies are pinned in `uv.lock`

## Statistical Methods

- **Pairwise**: Wilcoxon signed-rank, paired t-test, auto (Shapiro-Wilk selection)
- **Omnibus**: Friedman test, Nemenyi post-hoc with Critical Difference diagrams
- **Bayesian**: Signed-rank test with ROPE (Region of Practical Equivalence)
- **Effect sizes**: Cliff's delta (non-parametric), Cohen's d (parametric)
- **Corrections**: Holm-Bonferroni, Bonferroni
- **Confidence intervals**: BCa bootstrap
- **Power analysis**: Post-hoc power with recommended sample size
- **Multi-dataset**: Cross-dataset Friedman analysis (Demsar 2006)

## License

[Apache 2.0](LICENSE)
