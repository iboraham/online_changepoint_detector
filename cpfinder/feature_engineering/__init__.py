import numpy as np


def _get_cps_from_R(R: np.ndarray, insensivity_index: int) -> np.ndarray:
    cps = []
    y = 0

    maxes = R.argmax(axis=1)
    for x in range(R.shape[0] - 1):
        current_prob = R[x, y]
        next_prob = R[x + 1, y + 1]
        if current_prob > next_prob * insensivity_index:
            cps.append(x)
            y = maxes[x + 1]
            continue
        y += 1
    return cps
