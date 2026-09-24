import numpy as np

def winsorize(data: list, lo_q: float, hi_q: float) -> np.ndarray:
    """
    Returns float64 slices of clipped values, lower mask, and upper mask.
    """

    arr = np.array(data, dtype=np.float64)

    lo = np.percentile(arr, lo_q, axis=0)
    hi = np.percentile(arr, hi_q, axis=0)

    clipped = np.clip(arr, lo, hi)

    lower_mask = (arr<lo).astype(np.float64)
    upper_mask = (arr>hi).astype(np.float64)

    return np.stack([clipped, lower_mask, upper_mask])
    
