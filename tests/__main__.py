import os, sys, inspect


def _add_parent_folder():
    currentdir = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe()))
    )
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)


_add_parent_folder()

# -----------------------------------------------------------------------

from cpfinder import cpfinder
from cpfinder.datasets import generate_normal_time_series


if __name__ == "__main__":
    data = generate_normal_time_series(3)
    detector = cpfinder(data=data, method="rulsif")
    detector.fit(animationFlag=True, interval=100, plotFlag=True)
    # detector.saveAnimationVideo("assets/animation.gif")
