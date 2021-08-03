from cpfinder.methods import bocpd
from cpfinder.methods import rulsif


def str_to_func(string: str):
    """
    convert method string to function

    Args:
        string (str): method name as function

    Returns:
        func: method
    """
    if string == "bocpd":
        return bocpd
    if string == "rulsif":
        return rulsif
