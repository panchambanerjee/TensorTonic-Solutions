import numpy as np

def scale_cols(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each column multiplied by its weight.
    """
    data = np.array(data, dtype=np.float64)
    weights = np.array(weights, dtype=np.float64)

    scaled = data * weights

    return scaled
