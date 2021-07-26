import pandas as pd
from tqdm import tqdm
import numpy as np
from utils import find_fp


def append_all_columns(master_data: list, sub_data, channel: list):
    """
    Append all the columns of sub_data to master_data and creates new dataframe

    Args:
        master_data (list): master_data as target
        sub_data (pd.DataFrame): sub_data as source
        channel (list): a list includes organization name, uuid, channel name, phase information in order.
    """

    # Read channel information
    org_name, uuid, _, channel_name, phase = channel

    # append subdata to masterdata
    length = len(sub_data)
    master_data.append([org_name]*length)
    master_data.append([uuid]*length)
    master_data.append([channel_name]*length)
    master_data.append([phase]*length)
    master_data.append(sub_data.datetime)
    master_data.append(sub_data.ts)
    master_data.append(sub_data.P)
    master_data.append(sub_data.E)
    master_data.append(sub_data.PF)


def create_md(DATA_CHANNELS: pd.DataFrame, PATH: str):
    """Creates master data from version 1 file system. 

    Args:
        DATA_CHANNELS (pd.DataFrame): A dataframe of data-channels.csv file from version 1 file system.
    """
    master_data = []
    for i, channel in enumerate(tqdm(DATA_CHANNELS.to_numpy())):
        temp = []
        energy_data_fp = find_fp(channel, PATH)
        energy_data = pd.read_csv(energy_data_fp)
        append_all_columns(temp, energy_data, channel)
        temp = np.array(temp).T
        master_data.extend(temp)
    master_data = np.array(master_data)
    print(master_data.shape)
    master_data = pd.DataFrame(master_data, columns=[
                               'org', 'uuid', 'channel_name', 'phase', 'datetime', 'ts', 'P', 'E', 'PF'])
    master_data.to_csv("../Dataset/master_data.csv")
