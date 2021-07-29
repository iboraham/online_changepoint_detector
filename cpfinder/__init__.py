# Various feature engineering functions
from .feature_engineering import clean_data
from .utils import str_to_func
import pandas as pd


class cpfinder:
    def __init__(self, data: pd.DataFrame, method: str):
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

    def fit(self):

        # Given method to function
        method = str_to_func(self.method)

        detector = method("auto")
        return detector.fit(self.data)
