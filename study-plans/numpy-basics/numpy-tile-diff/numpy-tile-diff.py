import numpy as np

def tile_diff(data: list, reps: int) -> np.ndarray:
    """
    Returns float64 slices of tiled values and next-row differences with a final zero row.
    """

    arr = np.array(data, dtype=np.float64)

    tiled = np.tile(arr, (reps, 1))
    diff = np.diff(tiled, axis=0)

    diff_padded = np.pad(diff, ((0,1), (0,0)))

    return np.stack([tiled, diff_padded])
    
