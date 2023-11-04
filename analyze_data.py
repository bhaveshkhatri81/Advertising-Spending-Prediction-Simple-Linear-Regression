import regression_analysis
import pandas as pd
import numpy as np
import verification
import matplotlib.pyplot as plt

excel = pd.read_excel('Data set\CO2-by-source.xlsx', 'Training data') #Read the excel file and get the sheet called "Training data"

#Compute for the first peice of the function
x_train = np.array(excel["Year (0-5)"].dropna().to_numpy()) #This line will get the data from the column called "Year (0-5)" and convert it into a numpy array
y_train = np.array(excel["Total sum excluding flaring"].dropna().to_numpy()) #This line will get the data from the column called "Total sum excluding flaring" and convert it into a numpy array
optimized_params_first = regression_analysis.analyze(x_train, y_train, initial_guess=np.zeros(3)) #This line will perform the regression analysis on the data set
print("loss: ", verification.compute_loss(x_plot=x_train, y_plot=y_train, function=regression_analysis.nonlinear_func, params=optimized_params_first)) #This line will compute the loss of the regression analysis

#Compute for the second peice of the function
x_train = np.array(excel["Year (6-13)"].dropna().to_numpy()) #This line will get the data from the column called "Year (6-13)" and convert it into a numpy array
y_train = np.array(excel["Total sum including flaring"].dropna().to_numpy())#This line will get the data from the column called "Total sum including flaring" and convert it into a numpy array
#Compute for the second sector of the function
optimized_params_second = regression_analysis.analyze(x_train, y_train, initial_guess=np.zeros(3))#This line will perform the regression analysis on the data set
print("loss: ", verification.compute_loss(x_plot=x_train, y_plot=y_train, function=regression_analysis.nonlinear_func, params=optimized_params_second))#This line will compute the loss of the regression analysis


#Read the excel file and get the sheet called "Combined Data".
#The combined data is the data that replace no data with for flaring.
excel = pd.read_excel('Data set\CO2-by-source.xlsx', 'Combined Data')

x_train = np.array(excel["Year"].dropna().to_numpy())#This line will get the data from the column called "Year" and convert it into a numpy array
y_train = np.array(excel["Total sum"].dropna().to_numpy())#This line will get the data from the column called "Total sum" and convert it into a numpy array
optimized_params = regression_analysis.analyze(x_train, y_train, initial_guess=np.zeros(3))#This line will perform the regression analysis on the data set
print("loss: ", verification.compute_loss(x_plot=x_train, y_plot=y_train, function=regression_analysis.nonlinear_func, params=optimized_params))#This line will compute the loss of the regression analysis


import graph_piecewise

y_piece = graph_piecewise.piecewise_func(x_train, optimized_params_first, optimized_params_second)#This line will compute the piecewise function
plt.plot(x_train, y_piece, 'o', label='data')
plt.show()