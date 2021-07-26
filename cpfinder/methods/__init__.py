from vis import plot_matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import roerich
from . import online_changepoint_detection as oncd
from . import online_rulsif as orul
from cpfinder.feature_engineering import _get_cps_from_R


class bocpd:
    """
    Creates animatation of the Bayesian Online Changepoint Detection by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/0710.3742

    """

    def __init__(self, args):
        if args == "auto":
            self.hazard = 1 / 100
            self.mean0 = 0
            self.var0 = 1
            self.varx = 2
            self.ii = 3
        else:
            self.hazard = args[0]
            self.mean0 = args[1]
            self.var0 = args[2]
            self.varx = args[3]
            self.ii = args[4]

    def fit(self, data, interval=100, animation=True):

        # Create model
        model = oncd.GaussianUnknownMean(self.mean0, self.var0, self.varx)

        if animation == True:
            # Plot
            animation = oncd.online_changepoint_detection_animation(
                data, model, self.hazard, interval, self.ii
            )
            plt.show()
            return animation
        else:
            R, pmean, pvar = oncd.online_changepoint_detection(
                data, model, self.hazard, self.ii
            )
            cps = _get_cps_from_R(R, self.ii)
            # fig, axes = plt.subplots(2, 1, figsize=(20, 10))
            # plot_matplotlib(axes, data, R, pmean, pvar, cps)
            # plt.show()
            return cps


class rulsif:
    """
    Creates animatation of the Generalization of Change-Point Detection
    in Time Series Data Based on Direct Density Ratio Estimation by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/2001.06386

    """

    def __init__(self, *args):
        if args[0] == "auto":
            self.model = roerich.OnlineNNRuLSIF(
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
                alpha=0.001,
            )
        else:
            self.model = roerich.OnlineNNRuLSIF(*args)

    def fit(self, data, interval, plot=True):
        T = np.arange(len(data))

        # Create
        d = data.flatten()
        try:
            score, peaks = self.model.predict(d)
        except ValueError or TypeError:
            peaks = []

        # fig = plt.figure(figsize=(12, 20))
        # ani = FuncAnimation(
        #     fig,
        #     orul.animate_rulsif,
        #     np.arange(500, len(data), 500),
        #     fargs=(data, [], self.model),
        # )
        # plt.show()

        if plot == True:
            data = data.reshape(-1, 1)
            roerich.display(data, T, [], score, T, peaks=peaks)
            plt.show()

        return peaks
