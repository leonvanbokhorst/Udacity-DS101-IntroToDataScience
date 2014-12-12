import numpy as np


def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    d = np.array(data)
    p = np.array(predictions)
    m = np.mean(d)

    r_squared = 1 - np.square(d - p).sum() / np.square(d - m).sum()

    return r_squared


data = [1, 2, 3, 4, 5]
predictions = [1, 3, 2, 4, 5]
print(compute_r_squared(data, predictions))