from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import roerich
from cpfinder.vis import roerich_display_edited
from cpfinder.utils import find_peaks


def online_changepoint_detector(X):
    """
    Creates animatation of the Generalization of Change-Point Detection
    in Time Series Data Based on Direct Density Ratio Estimation by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/2001.06386
        https://github.com/HSE-LAMBDA/roerich

    Args:
        X (Array-like): Time series values that changepoint detector will work on

    Returns:
        array-like: score of the change point
        array-like: peak points
    """
    T = np.arange(len(X))

    cpd = roerich.OnlineNNRuLSIF(
        net="default",
        scaler="default",
        metric="KL_sym",
        periods=1,
        window_size=10,
        lag_size=500,
        step=10,
        n_epochs=10,
        lr=0.1,
        lam=0.0001,
        optimizer="Adam",
        alpha=0.1,
    )

    score, peaks = cpd.predict(X)
    return score, peaks


def animate_rulsif(i, *args):
    data, L, cpd = args
    X = data[:i]
    X = np.array(X).reshape(-1, 1)
    T = np.arange(len(X))
    Ts = T
    try:
        score, _ = cpd.predict(X)
        peaks = find_peaks(score)
    except ValueError or TypeError:
        score, peaks = np.zeros(len(X)), None

    n = X.shape[1] + 1 if peaks is None else X.shape[1] + 2
    _plot(X, score, peaks, L, n)


def _plot(X, score, peaks, annots, n):
    T = np.arange(len(X))
    roerich_display_edited(X, n, T, annots, score, T, peaks)
