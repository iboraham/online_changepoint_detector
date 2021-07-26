import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


def plot_posterior(axes, data, R, pmean, pvar, cps):
    T = len(data)
    ax1, ax2 = axes
    ax1.cla()
    ax1.scatter(range(0, T), data)
    ax1.plot(range(0, T), data)
    ax1.set_xlim([0, T])
    ax1.margins(0)

    # Plot predictions.
    ax1.plot(range(0, T), pmean, c="k")
    _2std = 2 * np.sqrt(pvar)
    ax1.plot(range(0, T), pmean - _2std, c="k", ls="--")
    ax1.plot(range(0, T), pmean + _2std, c="k", ls="--")

    ax2.cla()
    ax2.imshow(
        np.rot90(R), aspect="auto", cmap="gray_r", norm=LogNorm(vmin=0.0001, vmax=1)
    )
    ax2.set_xlim([0, T])
    ax2.margins(0)

    for cp in cps:
        ax1.axvline(cp, c="red", ls="dotted")
        ax2.axvline(cp, c="red", ls="dotted")

    plt.tight_layout()


def _plot(axes, d, R, pmean, pvar):
    T = len(d)
    ax1, ax2 = axes

    ax1.scatter(range(0, T), d)
    ax1.plot(range(0, T), d)
    ax1.set_xlim([0, T])
    ax1.margins(0)

    # Plot predictions.
    ax1.plot(range(0, T), pmean, c="k")
    _2std = 2 * np.sqrt(pvar)
    ax1.plot(range(0, T), pmean - _2std, c="k", ls="--")
    ax1.plot(range(0, T), pmean + _2std, c="k", ls="--")

    ax2.cla()
    ax2.imshow(
        np.rot90(R), aspect="auto", cmap="gray_r", norm=LogNorm(vmin=0.0001, vmax=1)
    )
    ax2.set_xlim([0, T])
    ax2.margins(0)
