import numpy
import pandas


def compute_cost(predicted_values, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features
    (input data points) and values (output data points).
    """
    m = len(values)

    sum_of_square_errors = numpy.square(predicted_values - values).sum()
    cost = sum_of_square_errors / (2 * m)

    return cost


def calculate_predicted_values(features, theta):
    """
    Calculate the sum of the predicted values given the featuire set and theta's
    """
    predicted_values = numpy.dot(features, theta)

    return predicted_values


def calculate_theta(alpha, features, predicted_values, theta, values):
    """
    Calculate the new theta given the predicted values vs the actual values
    """

    m = len(values) * 1.0
    theta -= (alpha / m) * numpy.dot((predicted_values - values), features)

    return theta


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # features  : Input data points (x) sums of all xi*theta
    # values    : Outpout data points (y)
    # theta     : Theta vector for the corresponding feature vector
    # alpha     : Step size
    # num_iter  : Number of iterations

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it
    # to cost_history.
    # See the Instructor notes for hints.

    cost_history = []

    for i in range(0, num_iterations):
        # Calculate the predicted values
        predicted_values = calculate_predicted_values(features, theta)

        # Gradient Descent in action:
        theta = calculate_theta(alpha, features, predicted_values, theta, values)

        # Calculate cost
        cost = compute_cost(predicted_values, values, theta)

        # Append cost to history
        cost_history.append(cost)

    return theta, pandas.Series(cost_history)


featrs = [172.0, 174.0, 185.0]
values = [254.0, 173.0, 184.0]
thetas = [1.0, 2.0, 3.0]
print gradient_descent(featrs, values, thetas, .005, 100)