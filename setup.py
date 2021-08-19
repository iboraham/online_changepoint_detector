from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="cpfinder",
    packages=[
        "cpfinder",
        "cpfinder.datasets",
        "cpfinder.eval_metrics",
        "cpfinder.feature_engineering",
        "cpfinder.methods",
        "cpfinder.utils",
        "cpfinder.vis",
    ],
    version="0.2.1",
    license="MIT",
    description="Online changepoint detection for python",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ibrahim Onur Serbetci",
    author_email="ionurserbetci@gmail.com",
    url="https://github.com/iboraham/online_changepoint_detector",
    download_url="https://github.com/iboraham/online_changepoint_detector/archive/v_02.tar.gz",
    keywords=[
        "online changepoint detection",
        "changepoint detection",
        "rulsif",
        "bayesian",
    ],
    install_requires=[
        "cycler>=0.10.0",
        "densratio>=0.2.2",
        "joblib>=1.0.1",
        "kiwisolver>=1.3.1",
        "matplotlib>=3.4.2",
        "numpy>=1.21.1",
        "pandas>=1.3.1",
        "Pillow>=8.3.1",
        "plotly>=5.1.0",
        "pytz>=2021.1",
        "roerich>=0.1",
        "scikit-learn>=0.24.2",
        "scipy>=1.7.1",
        "sklearn>=0.0",
        "tenacity>=8.0.1",
        "threadpoolctl>=2.2.0",
        "torch>=1.9.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
