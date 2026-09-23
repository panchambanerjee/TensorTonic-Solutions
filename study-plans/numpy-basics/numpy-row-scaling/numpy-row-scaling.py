import numpy as np

def scale_rows(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each row multiplied by its weight.
    """

    data = np.array(data, dtype=np.float64)
    weights = np.array(weights, dtype=np.float64)

    result = data * weights[:, np.newaxis]

    return result
