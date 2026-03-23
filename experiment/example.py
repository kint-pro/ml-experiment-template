import numpy as np
from ml_experiment_stats import ExperimentConfig, RunResult, set_seed


def generate_data(config: ExperimentConfig, seed: int):
    rng = np.random.RandomState(seed)
    n = config.data.n_train + config.data.n_val + config.data.n_test
    n_features = 10
    x = rng.randn(n, n_features)

    true_weights = np.zeros(n_features)
    true_weights[:5] = [3.0, -2.0, 1.5, -1.0, 0.5]
    y = x @ true_weights + rng.randn(n) * 0.5

    n_train = config.data.n_train
    n_val = config.data.n_train + config.data.n_val
    return (
        x[:n_train], y[:n_train],
        x[n_train:n_val], y[n_train:n_val],
        x[n_val:], y[n_val:],
    )


def fit_linear(x_train, y_train):
    return np.linalg.lstsq(x_train, y_train, rcond=None)[0]


def fit_ridge(x_train, y_train, alpha=1.0):
    n_features = x_train.shape[1]
    return np.linalg.solve(
        x_train.T @ x_train + alpha * np.eye(n_features),
        x_train.T @ y_train,
    )


def fit_lasso_cd(x_train, y_train, alpha=0.1, max_iter=1000, tol=1e-4):
    n_samples, n_features = x_train.shape
    weights = np.zeros(n_features)
    for _ in range(max_iter):
        weights_old = weights.copy()
        for j in range(n_features):
            residual = y_train - x_train @ weights + x_train[:, j] * weights[j]
            rho = x_train[:, j] @ residual / n_samples
            norm = (x_train[:, j] ** 2).sum() / n_samples
            weights[j] = np.sign(rho) * max(abs(rho) - alpha, 0) / norm
        if np.max(np.abs(weights - weights_old)) < tol:
            break
    return weights


def mse(y_true, y_pred):
    return float(np.mean((y_true - y_pred) ** 2))


def run_single(config: ExperimentConfig, seed: int) -> list[RunResult]:
    set_seed(seed)
    x_train, y_train, x_val, y_val, x_test, y_test = generate_data(config, seed)

    methods = {
        "linear": fit_linear,
        "ridge": lambda x, y: fit_ridge(x, y, alpha=1.0),
        "lasso": lambda x, y: fit_lasso_cd(x, y, alpha=0.1),
    }

    results = []
    for name, fit_fn in methods.items():
        weights = fit_fn(x_train, y_train)
        test_mse = mse(y_test, x_test @ weights)
        val_mse = mse(y_val, x_val @ weights)
        n_nonzero = int(np.sum(np.abs(weights) > 1e-6))
        results.append(RunResult(
            seed=seed,
            method=name,
            metrics={"mse": test_mse, "val_mse": val_mse},
            metadata={"n_nonzero_weights": n_nonzero},
        ))

    return results
