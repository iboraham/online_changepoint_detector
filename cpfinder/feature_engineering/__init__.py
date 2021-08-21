import numpy as np
from scipy.signal import find_peaks as fp


def _get_cps_from_R(R: np.ndarray, insensivity_index: int) -> np.ndarray:
    return (
        fp(np.flipud(np.rot90(R))[insensivity_index, :], height=0.05, distance=None)[0][
            1:
        ]
        - insensivity_index
    )
