import numpy as np
"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # parameters 
    N = 0
    sum = 0
    sum_sqrd = 0 

    # summing the sequence for mean
    for el in x:
        N += 1
        sum += el

    # summing the sequence for mean of squares
    for el in x:
        sum_sqrd += el ** 2

    # calculate mean and mean of squares
    mean = (1 / N) * sum
    mean_of_sqrs = (1 / N) * sum_sqrd 
    
    # calculate variance and standsrd deviation
    variance = (mean_of_sqrs - mean ** 2) 
    sd = variance ** (1/2)

    return sd 

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # parameters
    N = len(x) 
    sum_x = sum(x)
    sum_x_sqrd = sum(e*e for e in x)

    # calculate mean and mean of squares
    mean = (1 / N) * sum_x
    mean_of_sqrs = (1 / N) * sum_x_sqrd 
    
    # calculate variance and standsrd deviation
    variance = (mean_of_sqrs - mean ** 2) 
    sd = variance ** (1/2)

    return sd 

num_lst = [1, 2, 3, 4, 5]

# test run and NumPy's std function showcase
print(std_builtin(num_lst))
print(std_loops(num_lst))
print(np.std(num_lst))
    
    
