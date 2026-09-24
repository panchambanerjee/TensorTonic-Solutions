import numpy as np

def norm_gate(X: list, W: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    
    X = np.array(X, dtype=np.float64)
    W = np.array(W, dtype=np.float64) 

    Y = X @ W
    norms = np.linalg.norm(Y, axis=1)

    gate = (norms >= threshold).astype(np.float64)

    return Y * gate[:, np.newaxis]
    