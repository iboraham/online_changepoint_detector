from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import roerich


def animate_rulsif(i, *args):
    data, L, cpd = args
    X = data[:i]
    X = np.array(X).reshape(-1, 1)
    T = np.arange(len(X))
    Ts = T
    S, peaks = cpd.predict(X)

    plot_peak_height = 10
    s_max = 10

    n = X.shape[1] + 1 if peaks is None else X.shape[1] + 2
    for i in range(X.shape[1]):

        plt.subplot(n, 1, i + 1)
        ax = X[:, i]
        plt.plot(T, ax, linewidth=2, label="Original signal", color="C0")
        for t in T[L == 1]:
            plt.plot([t] * 2, [ax.min(), ax.max()], color="0", linestyle="--")
        plt.ylim(ax.min(), ax.max())
        plt.xlim(0, T.max())
        plt.xticks(size=16)
        plt.yticks(size=16)
        plt.legend(loc="upper left", fontsize=16)
        plt.tight_layout()

    score_plot_ix = n if peaks is None else n - 1
    plt.subplot(n, 1, score_plot_ix)
    plt.plot(Ts, S, linewidth=3, label="Change-point score", color="C3")
    for t in T[L == 1]:
        plt.plot([t] * 2, [-1, s_max], color="0", linestyle="--")

    # display find peaks #todo refactoring
    if peaks is not None:
        plt.subplot(n, 1, n)
        new_score_peaks = np.zeros(len(T))
        new_score_peaks[peaks] = plot_peak_height
        plt.plot(new_score_peaks, linewidth=3, label="Peaks", color="C4")
        for t in T[L == 1]:
            plt.plot([t] * 2, [-1, s_max], color="0", linestyle="--")

    plt.ylim(-1, s_max)
    plt.xlim(0, T.max())
    plt.xticks(size=16)
    plt.yticks(np.arange(0, s_max + 1, 5), size=16)
    plt.xlabel("Time", size=16)
    plt.legend(loc="upper left", fontsize=16)
    plt.tight_layout()


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


def online_changepoint_detector_animation(X):
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
    fig = plt.figure(figsize=(12, 20))
    ani = FuncAnimation(
        fig,
        animate_rulsif,
        np.arange(500, len(X), 500),
        fargs=(X, [], cpd),
    )
    plt.show()


def _plot(X, score, peaks):
    T = np.arange(X)
    roerich.display(X, T, L=[], S=score, Ts=T, peaks=peaks)
