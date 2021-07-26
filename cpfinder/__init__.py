# Various feature engineering functions
from .feature_engineering import clean_data
from .utils import str_to_func
import pandas as pd


class cpfinder:
    def __init__(
        self, data: pd.DataFrame, method: str, channel_id: str, interval: int = 100
    ):
        """
        Finds the changepoints with various methods.

        Args:
            method (str): A method to find changepoint including; BOCPD (as Bayesian Online Chanpoint Detection), rulsif (as online RuLSif)..
            data (pd.DataFrame): Time series that changepoint detector will work on
            channel_id (str): [description]
            interval (int, optional): Animation variable to use to determine how much sample in each step. Defaults to 100.
        """
        self.method = method
        self.data = data
        self.channel_id = channel_id
        self.interval = interval

    def fit(self):
        # Data prep.
        self.data, self.dt = clean_data(self.data, self.channel_id)

        # Divide the P,PF,E data
        power = self.data[:, 0]
        power_factor = self.data[:, 1]
        energy = self.data[:, 2]

        # Given method to function
        method = str_to_func(self.method)

        # Power
        detector = method("auto")
        cps_p = detector.fit(power, self.interval)
        cps_pf = detector.fit(power_factor, self.interval)
        cps_e = detector.fit(energy, self.interval)
        return cps_p, cps_pf, cps_e
