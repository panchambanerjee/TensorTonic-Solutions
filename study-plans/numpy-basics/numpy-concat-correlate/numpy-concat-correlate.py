import numpy as np

def compare_correlations(a: list, b: list) -> np.ndarray:
    """
    Returns float64 correlation matrices for a, b, and their combined rows.
    """

    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)

    a_and_b = np.concatenate([a, b], axis=0)

    a_corr = np.corrcoef(a.T)
    b_corr = np.corrcoef(b.T)

    a_and_b_corr = np.corrcoef(a_and_b.T)

    return np.stack([a_corr, b_corr, a_and_b_corr])