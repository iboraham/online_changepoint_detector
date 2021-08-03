import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.dates as mdates


def plot_posterior(
    data, dt, R, pmean, pvar, cps, title=None, save=False, save_name=None
):
    T = len(data)
    fig, axes = plt.subplots(2, 1, figsize=(20, 8))
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = "20"
    fig.suptitle(title, fontsize=24)
    fig.autofmt_xdate()
    ax1, ax2 = axes
    ax1.cla()
    ax1.scatter(dt, data)
    ax1.plot(dt, data)
    ax1.set_xlim([dt[0], dt[-1]])
    ax1.margins(0)

    # Plot predictions.
    ax1.plot(dt, pmean, c="k", label="Mean Prediction")
    _2std = 2 * np.sqrt(pvar)
    ax1.plot(dt, pmean - _2std, c="k", ls="--", label="Mean Prediction +- 2std")
    ax1.plot(dt, pmean + _2std, c="k", ls="--")

    ax2.cla()
    ax2.imshow(
        np.rot90(R), aspect="auto", cmap="gray_r", norm=LogNorm(vmin=0.0001, vmax=1)
    )
    maxes = R.argmax(axis=1)
    ax2.plot(len(R) - maxes, c="r", linewidth=3, label="Maxes")
    ax2.set_xlim([0, T])
    ax2.margins(0)

    for cp in cps:
        ax1.axvline(cp, c="red", ls="dotted", label="Ground Truths")
        ax2.axvline(cp, c="red", ls="dotted")

    plt.tight_layout()
    handles, labels = [
        (a + b)
        for a, b in zip(
            ax1.get_legend_handles_labels(), ax2.get_legend_handles_labels()
        )
    ]
    fig.legend(handles, labels)
    if save:
        plt.savefig(save_name)


def plot_posterior_animation(data, fig, axes, dt, R, pmean, pvar, cps, title=None):
    T = len(data)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = "20"
    fig.suptitle(title, fontsize=24)
    fig.autofmt_xdate()
    ax1, ax2 = axes
    ax1.cla()
    ax1.scatter(dt, data)
    ax1.plot(dt, data)
    ax1.set_xlim([dt[0], dt[-1]])
    ax1.margins(0)

    # Plot predictions.
    ax1.plot(dt, pmean, c="k", label="Mean Prediction")
    _2std = 2 * np.sqrt(pvar)
    ax1.plot(dt, pmean - _2std, c="k", ls="--", label="Mean Prediction +- 2std")
    ax1.plot(dt, pmean + _2std, c="k", ls="--")

    ax2.cla()
    ax2.imshow(
        np.rot90(R), aspect="auto", cmap="gray_r", norm=LogNorm(vmin=0.0001, vmax=1)
    )
    maxes = R.argmax(axis=1)
    ax2.plot(len(R) - maxes, c="r", linewidth=3, label="Maxes")
    ax2.set_xlim([0, T])
    ax2.margins(0)

    for cp in cps:
        ax1.axvline(cp, c="red", ls="dotted", label="Ground Truths")
        ax2.axvline(cp, c="red", ls="dotted")

    plt.tight_layout()
    handles, labels = [
        (a + b)
        for a, b in zip(
            ax1.get_legend_handles_labels(), ax2.get_legend_handles_labels()
        )
    ]
    fig.legend(handles, labels)
