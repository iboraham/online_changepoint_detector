from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LogNorm
import numpy as np
import pandas as pd
import argparse
from sklearn.preprocessing import scale
import roerich

# Creates eda_img file to obtain intial knowledge about data
from vis import initial_plot, plot_result
from vis import plot_matplotlib

# Creates the master data
from create_master_data import create_md

# cpfinder - custom module
from cpfinder import cpfinder

# -----------------------------------------------------------------------------------


# Dataset path
DATA_DIR = "../Dataset"

# Data_channels table
DATA_CHANNELS = pd.read_csv(DATA_DIR + "/data-channels.csv")

# Masterdata
master = pd.read_csv(DATA_DIR + "/master_data.csv")


def main(args):
    # Parse args
    method = args.method
    channel_id = args.channel_id
    interval = int(args.interval)
    plot_flag = args.plot
    evaluate_flag = args.evaluate

    cpd = cpfinder(master, method, channel_id, interval)
    cps_p, cps_pf, cps_e = cpd.fit()

    # f = r"animation.gif"
    # writergif = animation.PillowWriter(fps=1)
    # cps_p.save(f, writer=writergif)
    
    if plot_flag:
        plot_result(cpd, cps_p, cps_pf, cps_e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", default="BOCPD")
    parser.add_argument("-c", "--channel-id", default="0CCD0005")
    parser.add_argument("-i", "--interval", default="100")
    parser.add_argument("-p", "--plot", action="store_true")
    parser.add_argument("-e", "--evaluate", action="store_true")
    args = parser.parse_args()
    main(args)
