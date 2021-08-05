from matplotlib import pyplot as plt
from .plot_mtp import plot_posterior, plot_posterior_animation
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_matplotlib(*args):
    plot_posterior(*args)


def plot_matplotlib_animation(*args):
    plot_posterior_animation(*args)


def plot_result(cpd, cps_p, cps_pf, cps_e):
    fig, axes = plt.subplots(3, 1, figsize=(20, 8))
    axes[0].plot(cpd.data[:, 0])
    for cp in cps_p:
        axes[0].axvline(cp, color="r")
    axes[1].plot(cpd.data[:, 1])
    for cp in cps_pf:
        axes[1].axvline(cp, color="r")
    axes[2].plot(cpd.data[:, 2])
    for cp in cps_e:
        axes[2].axvline(cp, color="r")
    plt.show()
