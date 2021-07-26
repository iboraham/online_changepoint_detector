import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from tqdm import tqdm
from utils import find_fp
import pandas as pd


def plot(DATA_CHANNELS, PATH):
    for i, channel in enumerate(tqdm(DATA_CHANNELS.to_numpy())):
        energy_data_fp = find_fp(channel, PATH)
        energy_data = pd.read_csv(energy_data_fp)
        _plot(energy_data, channel)


def _plot(energy_data, channel):
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, x_title='Date')
    fig.add_trace(go.Scatter(x=energy_data['datetime'], y=energy_data.P, name='Power',
                             line=dict(color='firebrick', width=1)), row=1, col=1)
    fig.add_trace(go.Scatter(x=energy_data['datetime'], y=energy_data.E, name='Energy',
                             line=dict(color='royalblue', width=1)), row=2, col=1)
    fig.add_trace(go.Scatter(x=energy_data['datetime'], y=energy_data.PF, name='Power Factor',
                             line=dict(color='dimgray', width=1)), row=3, col=1)
    fig.update_layout(title_text=f'{channel[0]}, {channel[3]}')
    fig['layout']['yaxis']['title'] = 'P'
    fig['layout']['yaxis2']['title'] = 'E'
    fig['layout']['yaxis3']['title'] = 'PF'
    fig.write_image(f"eda_img/{channel[1]}_{channel[4]}.png")
