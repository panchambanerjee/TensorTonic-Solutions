import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)

    
    a_scaled = (np.clip(a, lo, hi)-lo)/(hi-lo)

    b_scaled = (np.clip(b, lo, hi)-lo)/(hi-lo)

    return np.abs(a_scaled - b_scaled)