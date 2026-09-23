import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """

    rng = np.random.default_rng(seed=seed)

    if kind=='uniform':
        return rng.random(tuple(shape), dtype=np.float64)
    return rng.standard_normal(tuple(shape), dtype=np.float64)
