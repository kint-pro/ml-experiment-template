from ml_experiment_stats import ExperimentConfig, RunResult, set_seed


def run_single(config: ExperimentConfig, seed: int) -> list[RunResult]:
    """Implement this function for your experiment.

    Called once per seed. Must return one RunResult per method.

    Args:
        config: Full experiment configuration (data sizes, model params, etc.)
        seed:   Random seed for this run (already set via set_seed)

    Returns:
        List of RunResult, one per method being compared. Example:

        [
            RunResult(seed=seed, method="baseline", metrics={"mse": 0.12, "acc": 0.93}),
            RunResult(seed=seed, method="proposed", metrics={"mse": 0.08, "acc": 0.96}),
        ]

        - seed: must match the seed argument
        - method: string name, consistent across seeds
        - metrics: dict of metric_name -> float (same keys for all methods)
        - metadata: optional dict for non-metric info (training time, etc.)
        - dataset: optional string for multi-dataset experiments (default: "default")

    See experiment/example.py for a complete working implementation.
    Run it with: make example
    """
    set_seed(seed)
    raise NotImplementedError("Implement run_single() for your experiment")
