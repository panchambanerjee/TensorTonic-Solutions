import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -> np.ndarray:
    """
    Returns a (2, n) float64 array: original row, then clipped row.
    """
    arr = np.array(data, dtype=np.float64)
    
    row_orig = arr[row_idx].copy()

    return np.stack([row_orig, np.clip(row_orig, lo, hi)])
    