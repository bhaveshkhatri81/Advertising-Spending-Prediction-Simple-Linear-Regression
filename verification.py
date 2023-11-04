import numpy as np

#The MSE is a common metric for evaluating the performance of regression models. It measures the average squared difference between the predicted and actual values of a function. A lower MSE indicates a better fit between the function and the data.
#This is function to calculate MSE.
def compute_loss(x_plot, y_plot, function, params):
    y_pred = function(x_plot, *params)
    mse = np.mean((y_plot - y_pred) ** 2)
    return mse