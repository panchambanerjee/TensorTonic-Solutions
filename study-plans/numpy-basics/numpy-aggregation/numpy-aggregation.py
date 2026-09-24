import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    
    arr = np.array(data, dtype=np.float64)

    arr_means = np.mean(arr, axis=axis)
    arr_std = np.std(arr, axis=axis)
    arr_min = np.min(arr, axis=axis)
    arr_max = np.max(arr, axis=axis)

    return np.stack([arr_means, arr_std, arr_min, arr_max])
    