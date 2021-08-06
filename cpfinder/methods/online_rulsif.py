import numpy as np
from cpfinder.vis import roerich_display_edited
from cpfinder.utils import find_peaks


def animate_rulsif(i, *args):
    data, L, cpd = args
    X = data[:i]
    X = np.array(X).reshape(-1, 1)
    T = np.arange(len(X))
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
