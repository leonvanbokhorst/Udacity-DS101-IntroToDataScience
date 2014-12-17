# coding=utf-8
import numpy as np
import pandas as pd
from ggplot import *
import matplotlib.pyplot as plt

def normalize_features(array):
    """
    Normalize the features in the data set.
    """
    array_normalized = (array - array.mean()) / array.std()
    mu = array.mean()
    sigma = array.std()

    return array_normalized, mu, sigma


def calculate_predicted_values(features, theta):
    """
    Calculate the sum of the predicted values given the feature set and theta's
    """
    predicted_values = np.dot(features, theta)

    return predicted_values


def calculate_theta(alpha, features, predicted_values, theta, values):
    """
    Calculate the new theta given the predicted values vs the actual values
    """

    m = len(values) * 1.0
    theta -= (alpha / m) * np.dot((predicted_values - values), features)

    return theta


def compute_cost(predicted_values, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    
    This can be the same code as the compute_cost function in the lesson #3 exercises,
    but feel free to implement your own.
    """

    m = len(values)
    sum_of_square_errors = np.square(predicted_values - values).sum()
    cost = sum_of_square_errors / (2 * m)

    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """

    cost_history = []

    for i in range(num_iterations):
        # Calculate the predicted values
        predicted_values = calculate_predicted_values(features, theta)

        # Gradient Descent in action:
        theta = calculate_theta(alpha, features, predicted_values, theta, values)

        # Calculate cost
        cost = compute_cost(predicted_values, values, theta)

        # Append cost to history
        cost_history.append(cost)

    return theta, pd.Series(cost_history)


def predictions(dataframe):
    # Select Features (try different features!)
    features = dataframe[['Weight', 'Shoesize']]

    # Values
    values = dataframe['Length']
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m)  # Add a column of 1s (y intercept)

    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

    # Set values for alpha, number of iterations.
    alpha = 0.05  # please feel free to change this value
    num_iterations = 100  # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array,
                                                            values_array,
                                                            theta_gradient_descent,
                                                            alpha,
                                                            num_iterations)

    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    #
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed
    # the 30 second limit on the compute servers.

    predictions = np.dot(features_array, theta_gradient_descent)
    r2 = compute_r_squared(values, predictions)

    return predictions, plot, r2, cost_history


def plot_cost_history(alpha, cost_history):
    """This function is for viewing the plot of your cost history.
    You can run it by uncommenting this

        plot_cost_history(alpha, cost_history)

    call in predictions.

    If you want to run this locally, you should print the return value
    from this function.
    """
    cost_df = pd.DataFrame({
        'Cost_History': cost_history,
        'Iteration': range(len(cost_history))
    })

    return ggplot(cost_df, aes('Iteration', 'Cost_History')) + geom_point() + ggtitle(
        'Cost History for alpha = %.3f' % alpha)


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


def plot_residuals(turnstile_weather, predictions):
    """
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    """

    plt.figure()
    (turnstile_weather['Length'] - predictions).hist()

    return plt



df = pd.read_csv(r"Data\lbo-test.csv")
print df

pred, plot, r2, costhist = predictions(df)
print pred
print r2
print plot
print costhist
# p = plot_residuals(df, pred)
# p.show()
