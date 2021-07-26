from matplotlib.colors import LogNorm
import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
from scipy.signal import find_peaks


def to_main_phase(data: pd.DataFrame):
    """Convert if phase is not main phase

    Args:
        data (pd.DataFrame): A master dataframe
    Returns:
        pd.DataFrame: a dataframe converted into columns of P, PF, and E
        according to their phase aggregate type e.g. mean, sum.
    """
    return (
        data.groupby(["org", "uuid", "datetime"])
        .agg({"P": "sum", "PF": "mean", "E": "sum"})
        .reset_index()
    )


def clean_data(data: pd.DataFrame, channel_id: str):
    # Group master data for given
    data_main_phase = to_main_phase(data)
    data_main_phase = data_main_phase[data_main_phase.uuid == channel_id]

    # Clean from na values
    data_clean = data_main_phase[~data_main_phase.isna().any(axis=1)]
    dt = data_clean.datetime
    data_clean = data_clean.iloc[:, 3:]

    # Standardize the data
    data = scale(data_clean)
    return data, dt


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
