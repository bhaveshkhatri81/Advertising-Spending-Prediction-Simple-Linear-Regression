# These are the libaries needed to perform the regression analysis on the data set
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def nonlinear_func(x, a, b, c):
        return a * np.exp(-b * x) + c # This is the form of the function that we are expecting


x_train = 0
y_train = 0
def analyze(x, y, initial_guess = [1, 1, 1]):
    x_train = x
    y_train = y
    # Plot the data to see what it looks like
    plt.plot(x_train, y_train, 'o')

    plt.show() #This command will show the data plot in a graph


    # Define the function to be used in the curve_fit function
    


    # Use the curve_fit function to fit the data to the function
    params, params_covariance = curve_fit(nonlinear_func, x_train, y_train, p0=initial_guess, maxfev=10000)
    #params is the optimized parameters, while the params_covariance is the covariance of the parameters
    #print(params_covariance)

    a_opt, b_opt, c_opt = params #Decompose the optimized parameters into individual variables

    # Create an array of optimized parameters
    optimized_params = np.array([a_opt, b_opt, c_opt])
    np.set_printoptions(precision=10)
    print("Optimized Parameters:", optimized_params) #Print out the optimized parameters

    y_plot = nonlinear_func(x_train, a_opt, b_opt, c_opt) #Generate the y values from the optimized parameters in terms of x

    plt.scatter(x_train, y_train, label='Actual Data') #The scatter function will make the data points appear as dots
    plt.plot(x_train, y_plot, 'r', label='Fitted Curve') #The plot function will make the fitted curve appear as a line
    print(x_train, y_plot)
    plt.show()
    return optimized_params