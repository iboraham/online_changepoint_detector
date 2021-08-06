import numpy as np
import pandas as pd
from scipy.signal import find_peaks as fp


def str_to_func(string: str):
    """
    convert method string to function

    Args:
        string (str): method name as function

    Returns:
        func: method
    """
    from cpfinder.methods import bocpd
    from cpfinder.methods import rulsif

    if string == "bocpd":
        return bocpd
    if string == "rulsif":
        return rulsif


def smoothen(x, winsize=5):
    return np.array(pd.Series(x).rolling(winsize).mean())[winsize - 1 :]


def find_peaks(score):
    return fp(score, height=1, distance=50)[0]
