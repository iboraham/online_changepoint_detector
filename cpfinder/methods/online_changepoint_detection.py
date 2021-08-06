from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.special import logsumexp
from tqdm import tqdm
from cpfinder.vis import plot_matplotlib_animation


# -----------------------------------------------------------------------------


def online_changepoint_detection_animation(data, model, hazard, interval=100, ii=1):
    """
    Creates animatation of the Bayesian Online Changepoint Detection by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/0710.3742


    Args:
        data (numpy.ndarray): Time series that changepoint detector will work on
        model (class): Estimation model
        hazard (float): Hazard function - see original paper for further inf.
        interval (int, optional): Animation variable to use to determine how much sample in each step. Defaults to 100.
    """
    # Animate
    fig, axes = plt.subplots(2, 1, figsize=(20, 10))
    ani = FuncAnimation(
        fig,
        _animate_bocpd,
        np.arange(1, len(data), interval),
        fargs=(fig, axes, data, model, hazard, interval, ii),
        interval=1,
        repeat=False,
    )
    return ani


def _animate_bocpd(i, fig, axes, data, model, hazard, interval=100, ii=1, annots=[]):
    if i == 1:
        d = data[:i]
    else:
        d = data[:i]

    T, log_R, pmean, pvar, log_message, log_H, log_1mH = _create_env(data, hazard, d)

    for t in tqdm(range(1, T + 1)):
        R, log_message = _calc(
            model, d, log_R, pmean, pvar, log_message, log_H, log_1mH, t
        )

    plot_matplotlib_animation(
        d, fig, axes, np.arange(0, len(d)), R, pmean, pvar, annots
    )


def online_changepoint_detection(
    data: np.ndarray, model, hazard: float, insensitivty_index: int
):
    """
    Creates animatation of the Bayesian Online Changepoint Detection by
    matplotlib.animation package.

    Org. Paper:
        https://arxiv.org/abs/0710.3742


    Args:
        data (numpy.ndarray): Time series that changepoint detector will work on
        model (class): Estimation model
        hazard (float): Hazard function - see original paper for further inf.
        interval (int, optional): Animation variable to use to determine how much sample in each step. Defaults to 100.
    """
    T, log_R, pmean, pvar, log_message, log_H, log_1mH = _create_env(data, hazard, data)

    for t in tqdm(range(1, T + 1)):
        R, log_message = _calc(
            model, data, log_R, pmean, pvar, log_message, log_H, log_1mH, t
        )
    return R, pmean, pvar


def _calc(model, d, log_R, pmean, pvar, log_message, log_H, log_1mH, t):
    x = d[t - 1]

    pmean[t - 1] = np.sum(np.exp(log_R[t - 1, :t]) * model.mean_params[:t])
    pvar[t - 1] = np.sum(np.exp(log_R[t - 1, :t]) * model.var_params[:t])

    log_pis = model.log_pred_prob(t, x)

    log_growth_probs = log_pis + log_message + log_1mH

    log_cp_prob = logsumexp(log_pis + log_message + log_H)

    new_log_joint = np.append(log_cp_prob, log_growth_probs)

    log_R[t, : t + 1] = new_log_joint
    log_R[t, : t + 1] -= logsumexp(new_log_joint)

    model.update_params(t, x)

    log_message = new_log_joint
    R = np.exp(log_R)
    return R, log_message


def _create_env(data, hazard, d):
    T = len(d)
    log_R = -np.inf * np.ones((T + 1, T + 1))
    log_R[0, 0] = 0  # log 0 == 1
    pmean = np.empty(T)
    pvar = np.empty(T)
    log_message = np.array([0])  # log 0 == 1
    log_H = np.log(hazard)
    log_1mH = np.log(1 - hazard)
    return T, log_R, pmean, pvar, log_message, log_H, log_1mH


# -----------------------------------------------------------------------------


class GaussianUnknownMean:
    def __init__(self, mean0, var0, varx):
        """Initialize model.

        meanx is unknown; varx is known
        p(meanx) = N(mean0, var0)
        p(x) = N(meanx, varx)
        """
        self.mean0 = mean0
        self.var0 = var0
        self.varx = varx
        self.mean_params = np.array([mean0])
        self.prec_params = np.array([1 / var0])

    def log_pred_prob(self, t, x):
        """Compute predictive probabilities \pi, i.e. the posterior predictive
        for each run length hypothesis.
        """
        # Posterior predictive: see eq. 40 in (Murphy 2007).
        post_means = self.mean_params[:t]
        post_stds = np.sqrt(self.var_params[:t])
        return norm(post_means, post_stds).logpdf(x)

    def update_params(self, t, x):
        """Upon observing a new datum x at time t, update all run length
        hypotheses.
        """
        # See eq. 19 in (Murphy 2007).
        new_prec_params = self.prec_params + (1 / self.varx)
        self.prec_params = np.append([1 / self.var0], new_prec_params)
        # See eq. 24 in (Murphy 2007).
        new_mean_params = (
            self.mean_params * self.prec_params[:-1] + (x / self.varx)
        ) / new_prec_params
        self.mean_params = np.append([self.mean0], new_mean_params)

    @property
    def var_params(self):
        """Helper function for computing the posterior variance."""
        return 1.0 / self.prec_params + self.varx
