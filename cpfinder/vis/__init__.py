from matplotlib import pyplot as plt
from .plot_mtp import plot_posterior, plot_posterior_animation
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_matplotlib(*args):
    plot_posterior(*args)


def plot_matplotlib_animation(*args):
    plot_posterior_animation(*args)


def plot_result(cpd, cps_p, cps_pf, cps_e):
    fig, axes = plt.subplots(3, 1, figsize=(20, 8))
    axes[0].plot(cpd.data[:, 0])
    for cp in cps_p:
        axes[0].axvline(cp, color="r")
    axes[1].plot(cpd.data[:, 1])
    for cp in cps_pf:
        axes[1].axvline(cp, color="r")
    axes[2].plot(cpd.data[:, 2])
    for cp in cps_e:
        axes[2].axvline(cp, color="r")
    plt.show()


def plot_result_plotly(cpd, cps_p, cps_pf, cps_e):
    channel_id = cpd.channel_id

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, x_title="Date")
    fig.add_trace(
        go.Scatter(
            x=cpd.dt,
            y=cpd.data[:, 0],
            name="Power",
            line=dict(color="firebrick", width=1),
        ),
        row=1,
        col=1,
    )
    for cp in cps_p:
        fig.add_vline(
            x=cpd.dt.iloc[cp],
            line_width=3,
            line_dash="dash",
            line_color="green",
            row=1,
            col=1,
        )

    fig.add_trace(
        go.Scatter(
            x=cpd.dt,
            y=cpd.data[:, 2],
            name="Energy",
            line=dict(color="royalblue", width=1),
        ),
        row=2,
        col=1,
    )
    for cp in cps_pf:
        fig.add_vline(
            x=cpd.dt.iloc[cp],
            line_width=3,
            line_dash="dash",
            line_color="green",
            row=2,
            col=1,
        )
    fig.add_trace(
        go.Scatter(
            x=cpd.dt,
            y=cpd.data[:, 1],
            name="Power Factor",
            line=dict(color="dimgray", width=1),
        ),
        row=3,
        col=1,
    )
    for cp in cps_e:
        fig.add_vline(
            x=cpd.dt.iloc[cp],
            line_width=3,
            line_dash="dash",
            line_color="green",
            row=3,
            col=1,
        )
    # fig.update_layout(title_text=f"{rest_name}, {channel_name}")
    fig.update_layout(title_text=f"{channel_id}")
    fig["layout"]["yaxis"]["title"] = "P"
    fig["layout"]["yaxis2"]["title"] = "E"
    fig["layout"]["yaxis3"]["title"] = "PF"
    return fig
