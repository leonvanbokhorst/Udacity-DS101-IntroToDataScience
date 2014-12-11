import numpy
import pandas


def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2 * m)

    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 

    cost_history = []
    m = len(values) * 1.0

    for i in range(0, num_iterations):
        # Calculate cost
        cost = compute_cost(features, values, theta)

        # Append cost to history
        cost_history.append(cost)

        # Calculate new theta
        theta += alpha * (1 / m) * numpy.dot((values - numpy.dot(features, theta)), features)

    return theta, pandas.Series(cost_history)  # leave this line for the grader


featrs = [1.2, 2.1, 3.9, 4.0, 1.9, 2.4]
values = [2.3, 3.6, 4.1, 5.2, 6.9, 7.7]
thetas = [0.05, 0.3, 0.15, 0.5, 0.05, 0.3]
print gradient_descent(featrs, values, thetas, .005, 100)