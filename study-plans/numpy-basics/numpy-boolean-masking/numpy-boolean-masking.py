import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    arr = np.array(data, dtype=np.float64)

    mask = arr>threshold

    elem_mask = mask # Can also do (mask).astype(np.float64) to direct get booleans
    any_mask = np.any(mask, axis=1)
    all_mask = np.all(mask, axis=1)

    elem_filtered = np.where(elem_mask, 1.0, 0.0)
    any_filtered = np.where(any_mask[:, np.newaxis], arr, 0.0)
    all_filtered = np.where(all_mask[:, np.newaxis], arr, 0.0)

    return np.stack([elem_filtered, any_filtered, all_filtered])