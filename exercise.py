import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Logic


def check_uniqueness(lst):
    """
    Check if a list contains only unique values.
    Returns True only if all values in the list are unique, False otherwise
    """

    # We first extract the unique values of lst
    length = np.unique(np.array(lst))
    
    return (length == len(lst))


def smallest_difference(array):
    """
    Code a function that takes an array and returns the smallest
    absolute difference between two elements of this array
    Please note that the array can be large and that the more
    computationally efficient the better
    """
    
    array = np.sort(array)
    diffMin=array.max()
    
    for i in range(len(array)-1):
        
        diff = abs(array[i]-array[i+1])
        
        if diff < diffMin :
            
            diffMin = diff
            
    return diffMin


# Finance and DataFrame manipulation


def macd(prices, window_short=12, window_long=26):
    """
    Code a function that takes a DataFrame named prices and
    returns it's MACD (Moving Average Convergence Difference) as
    a DataFrame with same shape
    Assume simple moving average rather than exponential moving average
    The expected output is in the output.csv file
    """
    
    # WE assume that the prices column is always at index 1 on the DataFrame
    
    mean_short_window = prices.iloc[:,1].rolling(window_short).mean()
    mean_long_window = prices.iloc[:,1].rolling(window_long).mean()
    
    prices["macd_12_26"] = mean_short_window - mean_long_window
    
    
    return prices


def sortino_ratio(prices):
    """
    Code a function that takes a DataFrame named prices and
    returns the Sortino ratio for each column
    Assume risk-free rate = 0
    On the given test set, it should yield 0.05457
    """
    
    # We'd simply add a 'for' loop on prices.iloc[:,i] if we have several stocks to treat 
    
    returns = prices.iloc[:,1].pct_change()[1:]
    
    returns_neg = returns[returns <= 0]
    
    downside_vol = returns_neg.std()
    
    mean = returns.mean()
    
    rf = 0
    
    sortino_ratio = (mean  - rf) / downside_vol
    
    
    return sortino_ratio


def expected_shortfall(prices, level=0.95):
    """
    Code a function that takes a DataFrame named prices and
    returns the expected shortfall at a given level
    On the given test set, it should yield -0.03468
    """
    # We skip the first value that should be NAN
    
    returns = prices.iloc[:,1].pct_change()[1:]
    
    VAR = np.quantile(returns,1-level)
    
    shortfall = returns[returns <= VAR].mean()
    
    return shortfall


# Plot


def visualize(prices, path):
    """
    Code a function that takes a DataFrame named prices and
    saves the plot to the given path
    """
    name = prices.iloc[:,1].name
    
    plt.plot(prices.iloc[:,1])
    
    plt.title(f"{name} stock price")
    plt.savefig(path + "/" + name + ".png")
    
    pass





