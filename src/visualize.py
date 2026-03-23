import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pyarrow.parquet as pq

from src.config import parse_args

COLORS = {
    0: "#2d3436",
    1: "#e17055",
    2: "#0984e3",
    3: "#00b894",
    4: "#6c5ce7",
}


def load_summary(results_dir: str) -> dict:
    path = Path(results_dir) / "summary.json"
    with open(path) as f:
        return json.load(f)


def load_metrics(results_dir: str) -> list[dict]:
    path = Path(results_dir) / "metrics.parquet"
    table = pq.read_table(path)
    return table.to_pylist()


def plot_comparison_bar(summary: dict, metric: str, output_dir: str, formats: list[str]):
    methods = [m for m in summary if metric in summary[m]]
    if not methods:
        return
    means = [summary[m][metric]["mean"] for m in methods]
    stds = [summary[m][metric]["std"] for m in methods]

    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.arange(len(methods))
    colors = [COLORS.get(i, COLORS[0]) for i in range(len(methods))]
    ax.bar(x, means, yerr=stds, color=colors, capsize=5, edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_ylabel(metric)
    ax.set_title(f"{metric} by Method")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()

    for fmt in formats:
        fig.savefig(Path(output_dir) / f"comparison_{metric}.{fmt}", dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_per_seed(rows: list[dict], metric: str, output_dir: str, formats: list[str]):
    methods = sorted(set(r["method"] for r in rows))
    seeds = sorted(set(int(r["seed"]) for r in rows))

    fig, ax = plt.subplots(figsize=(8, 4))
    for i, method in enumerate(methods):
        values = [
            float(r[metric]) for r in rows
            if r["method"] == method and r.get(metric) is not None
        ]
        color = COLORS.get(i, COLORS[0])
        ax.plot(seeds[: len(values)], values, "o-", label=method, color=color, markersize=4)

    ax.set_xlabel("Seed")
    ax.set_ylabel(metric)
    ax.set_title(f"{metric} Across Seeds")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()

    for fmt in formats:
        fig.savefig(Path(output_dir) / f"per_seed_{metric}.{fmt}", dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    config = parse_args()
    summary = load_summary(config.output.results_dir)
    rows = load_metrics(config.output.results_dir)

    Path(config.output.figures_dir).mkdir(parents=True, exist_ok=True)

    metrics = set()
    for method_data in summary.values():
        metrics.update(method_data.keys())

    for metric in sorted(metrics):
        plot_comparison_bar(summary, metric, config.output.figures_dir, config.output.figure_format)
        plot_per_seed(rows, metric, config.output.figures_dir, config.output.figure_format)


if __name__ == "__main__":
    main()
