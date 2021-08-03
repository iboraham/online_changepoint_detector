from cpfinder import cpfinder
from cpfinder.datasets import generate_normal_time_series

data = generate_normal_time_series(3)
detector = cpfinder(data=data, method="bocpd")
detector.fit(animationFlag=True, interval=100, plotFlag=False)
detector.saveAnimationVideo("assets/animation.gif")
