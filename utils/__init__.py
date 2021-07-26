from glob import glob


def find_fp(channel: list, PATH: str):
    """
    Finds registered filepath of the channel in the first version. 

    Args:
        channel (list): a list includes organization name, uuid, channel name, phase information in order. A row from "data-channels.csv" file.

    Returns:
        str: a filepath of the channel in first version file system. 
    """

    # Read each parameter of the channel
    org_name, uuid, _, channel_name, phase = channel
    # Check whether phase is system or not
    if phase == "system":
        fp = glob(
            f"{PATH}/{org_name}/{uuid[:4]}/{uuid.lower()}*.csv")[0]
    else:
        fp = glob(
            f"{PATH}/{org_name}/{uuid[:4]}/{uuid.lower()}*{phase}.csv")[0]
    return fp
