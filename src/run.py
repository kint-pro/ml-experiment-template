from pathlib import Path

from src.config import ExperimentConfig, parse_args
from src.results import ResultsCollector, RunResult
from src.seed import set_seed


def run_single(config: ExperimentConfig, seed: int) -> list[RunResult]:
    set_seed(seed)

    # TODO: Replace with actual experiment logic
    # This is the template structure. Each experiment implements its own version.
    #
    # Expected pattern:
    #   1. Generate or load data
    #   2. For each method:
    #      a. Train model
    #      b. Evaluate on test set
    #      c. Return RunResult with metrics
    #
    # Example:
    #   result = RunResult(
    #       seed=seed,
    #       method="method_name",
    #       metrics={"regret": 0.05, "mse": 0.12, "accuracy": 0.93},
    #       metadata={"epochs_trained": 87, "training_time_s": 12.4},
    #   )

    raise NotImplementedError("Implement run_single() for your experiment")


def main():
    config = parse_args()
    config.output.ensure_dirs()
    config.save(Path(config.output.results_dir) / "config_used.json")

    collector = ResultsCollector(config.output.results_dir)

    for seed in config.seed.seeds():
        print(f"[seed={seed}]")
        results = run_single(config, seed)
        for result in results:
            collector.add(result)
            primary_metric = next(iter(result.metrics), None)
            if primary_metric:
                print(f"  {result.method}: {primary_metric}={result.metrics[primary_metric]:.4f}")

    collector.save()
    print(f"\nResults saved to {config.output.results_dir}/")


if __name__ == "__main__":
    main()
