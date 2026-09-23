import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    arr = np.array(data, dtype=np.float64)

    norm_arr = (arr - arr.mean(axis=0))/(arr.std(axis=0))

    return norm_arr
