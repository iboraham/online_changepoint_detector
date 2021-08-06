from cpfinder.utils import find_peaks
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import roerich
from . import online_changepoint_detection as oncd
from . import online_rulsif as orul
from cpfinder.feature_engineering import _get_cps_from_R
from cpfinder.vis import plot_matplotlib, roerich_display_edited


class bocpd:
    """
    Creates animatation of the Bayesian Online Changepoint Detection by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/0710.3742

    """

    def __init__(self, args):
        if args["auto"]:
            self.hazard = 1 / 100
            self.mean0 = 0
            self.var0 = 1
            self.varx = 2
            self.ii = 3
        else:
            self.hazard = args["hazard"]
            self.mean0 = args["mean0"]
            self.var0 = args["var0"]
            self.varx = args["varx"]
            self.ii = args["ii"]

    def fit(self, data, interval, animationFlag, plotFlag, annots=[]):

        # Create model
        model = oncd.GaussianUnknownMean(self.mean0, self.var0, self.varx)

        if animationFlag == True:
            # Plot
            animation = oncd.online_changepoint_detection_animation(
                data, model, self.hazard, interval, self.ii
            )
            if plotFlag:
                plt.show()
            return animation
        else:
            R, pmean, pvar = oncd.online_changepoint_detection(
                data, model, self.hazard, self.ii
            )
            cps = _get_cps_from_R(R, self.ii)
            if plotFlag:
                plot_matplotlib(data, np.arange(0, len(data)), R, pmean, pvar, annots)
            return cps


class rulsif:
    """
    Creates animatation of the Generalization of Change-Point Detection
    in Time Series Data Based on Direct Density Ratio Estimation by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/2001.06386

    """

    def __init__(self, **args):
        if args["auto"]:
            self.model = roerich.OnlineNNRuLSIF(
                net="default",
                scaler="default",
                metric="KL_sym",
                periods=1,
                window_size=10,
                lag_size=100,
                step=10,
                n_epochs=10,
                lr=0.1,
                lam=0.0001,
                optimizer="Adam",
                alpha=0.1,
            )
        else:
            self.model = roerich.OnlineNNRuLSIF(**args)

    def fit(self, data, interval, animationFlag, plotFlag, annots=[]):
        T = np.arange(len(data))

        # Create
        d = data.flatten()

        if animationFlag:
            ani = self._animate_rulsif(interval, plotFlag, annots, d)
            return ani
        else:
            peaks = self._not_animate_rulsif(data, plotFlag, annots, T, d)
            return peaks

    def _not_animate_rulsif(self, data, plotFlag, annots, T, d):
        try:
            score, _ = self.model.predict(d)
            peaks = find_peaks(score)
        except ValueError or TypeError:
            peaks = []
        if plotFlag == True:
            data = data.reshape(-1, 1)
            n = data.shape[1] + 1 if peaks is None else data.shape[1] + 2
            roerich_display_edited(data, n, T, annots, score, T, peaks)
            plt.show()
        return peaks

    def _animate_rulsif(self, interval, plotFlag, annots, d):
        fig = plt.figure(figsize=(12, 6))
        ani = FuncAnimation(
            fig,
            orul.animate_rulsif,
            np.arange(1, len(d), interval),
            interval=1,
            repeat=False,
            fargs=(d, annots, self.model),
        )
        if plotFlag:
            plt.show()
        return ani
