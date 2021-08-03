from cpfinder import cpfinder
from cpfinder.datasets import generate_normal_time_series
import pandas as pd

data = generate_normal_time_series(100)
detector = cpfinder(data=data, method="bocpd")
detector.fit(animationFlag=False, interval=100, plotFlag=False)
print(detector.changepoints)
