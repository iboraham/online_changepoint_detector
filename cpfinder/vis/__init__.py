from matplotlib import pyplot as plt
from .plot_mtp import plot_posterior, plot_posterior_animation, display


def plot_matplotlib(*args):
    plot_posterior(*args)


def plot_matplotlib_animation(*args):
    plot_posterior_animation(*args)


def roerich_display_edited(*args):
    display(*args)


