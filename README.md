<h1 align="center">Welcome to CPFinder 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.22-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/iboraham/online_changepoint_detector/tree/master/docs" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://pepy.tech/project/cpfinder"><img src="https://pepy.tech/badge/cpfinder" alt="Downloads"></a>
  <img src='https://bettercodehub.com/edge/badge/iboraham/online_changepoint_detector?branch=master'>
  <a href="https://raw.githubusercontent.com/iboraham/online_changepoint_detector/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://lgtm.com/projects/g/iboraham/online_changepoint_detector/alerts/"><img alt="Total alerts" src="https://img.shields.io/lgtm/alerts/g/iboraham/online_changepoint_detector.svg?logo=lgtm&logoWidth=18"/></a>
  <a href="https://lgtm.com/projects/g/iboraham/online_changepoint_detector/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/iboraham/online_changepoint_detector.svg?logo=lgtm&logoWidth=18"/></a>
  
  <a href="https://colab.research.google.com/github/iboraham/online_changepoint_detector/blob/master/docs/example.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
  <a href="https://twitter.com/iboraham" target="_blank">
    <img alt="Twitter: iboraham" src="https://img.shields.io/twitter/follow/iboraham.svg?style=social" />
  </a>
</p>

> Online changepoint detection for python

### 🏠 [Homepage](https://github.com/iboraham/online_changepoint_detector)

### ✨ [Demo](https://github.com/iboraham/online_changepoint_detector/blob/master/assets/preview.gif?raw=true)

![Demo](https://github.com/iboraham/online_changepoint_detector/blob/master/assets/preview.gif?raw=true)

## Install

```sh
pip install cpfinder
```

## Usage

```sh
python example.py

 ---

# Import libraries
>> from cpfinder import cpfinder
>> from cpfinder.datasets import generate_normal_time_series

# Example data
>> data = generate_normal_time_series(totalPartitions=3)

# Changepoint Detection
>> detector = cpfinder(data=data, method="bocpd")
>> detector.fit(animationFlag=True, interval=100, plotFlag=False)
>> print(detector.changepoints)

'''
[171, 1538]
'''

# You can save animation as gif
>> detector.saveAnimationVideo("assets/animation.gif")
```

## Run tests

```sh
python tests
```

## Author

👤 **I.Onur Serbetci**

- Website: kaggle.com/onurserbetci
- Twitter: [@iboraham](https://twitter.com/iboraham)
- Github: [@iboraham](https://github.com/iboraham)
- LinkedIn: [@ionur-serbetci](https://linkedin.com/in/ionur-serbetci)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/iboraham/online_changepoint_detector/issues).

## Show your support

Give a ⭐️ if this project helped you!

<a href="https://www.patreon.com/iboraham">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2021 [I.Onur Serbetci](https://github.com/iboraham).<br />
This project is [MIT](https://raw.githubusercontent.com/iboraham/online_changepoint_detector/master/LICENSE) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
