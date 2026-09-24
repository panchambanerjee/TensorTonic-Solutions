import numpy as np

def quantize_and_frame(data: list, decimals: int, pad_width: int) -> np.ndarray:
    """
    Returns float64 slices of rounded, floored, and ceiling-rounded values with zero borders.
    """

    arr = np.array(data, dtype=np.float64)

    pad = lambda x: np.pad(x, pad_width, mode='constant', constant_values=0)

    arr_round = pad(np.round(arr, decimals))
    arr_floor = pad(np.floor(arr))
    arr_ceil = pad(np.ceil(arr))

    return np.stack([arr_round, arr_floor, arr_ceil])
