import numpy as np


def generate_normal_time_series(count: int, minNumber=50, maxNumber=1000, seed=42):
    """
    Function that return generated normal time series data for method testing.

    Args:
        count (int): Number of observation in the generated time series data.
        minNumber (int, optional): Maximum value in time series data. Defaults to 50.
        maxNumber (int, optional): Minimum value in time series data. Defaults to 1000.
        seed (int, optional): Seed to generate random numbers. Defaults to 42.

    Returns:
        np.ndarray: Generated normal time series
    """
    np.random.seed(seed)
    data = np.array([], dtype=np.float64)
    partition = np.random.randint(minNumber, maxNumber, count)
    for partitionSize in partition:
        partitionMean = np.random.randn() * 10
        partitionVar = np.random.randn() * 1
        if partitionVar < 0:
            partitionVar = partitionVar * -1 if partitionVar < 0 else partitionVar
        partitionData = np.random.normal(partitionMean, partitionVar, partitionSize)
        data = np.concatenate((data, partitionData))
    return data
