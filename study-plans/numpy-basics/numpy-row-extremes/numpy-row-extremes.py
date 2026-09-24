import numpy as np

def row_extremes(data: list) -> np.ndarray:
    """
    Returns float64 rows of maxima, maximum indices, minima, and minimum indices.
    """

    arr = np.array(data, dtype=np.float64)
    m = arr.shape[0]

    row_idx = np.arange(m)

    max_idx = np.argmax(arr, axis=1)
    min_idx = np.argmin(arr, axis=1)

    
    max_vals = arr[row_idx, max_idx]
    min_vals = arr[row_idx, min_idx]

    return np.stack([max_vals, max_idx.astype(np.float64), \
                    min_vals, min_idx.astype(np.float64)])
