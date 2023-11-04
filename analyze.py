import argparse
import os
import numpy as np


parser = argparse.ArgumentParser(description='Analyze data')
parser.add_argument('--excel_file_path', type=str, default='Data set\CO2-by-source.xlsx', help='Path to the excel file')

args = parser.parse_args()


excel_file_path = args.excel_file_path

#check if the file exists

if not os.path.exists(excel_file_path):
    raise Exception("File does not exist")


import verification
import regression_analysis
import pandas as pd

excel = pd.read_excel(excel_file_path, 'Training data') #Read the excel file and get the sheet called "Training data"

x_train = excel["x"]
y_train = excel["y"]

optimized_params = regression_analysis.analyze(x_train, y_train, initial_guess=np.zeros(3)) #This line will perform the regression analysis on the data set
print("loss: ", verification.compute_loss(x_plot=x_train, y_plot=y_train, function=regression_analysis.nonlinear_func, params=optimized_params)) #This line will compute the loss of the regression analysis

#Graph the data
import matplotlib.pyplot as plt
y_optimized = regression_analysis.nonlinear_func(x_train, *optimized_params)

plt.plot(x_train, y_train, 'o', label='data')
plt.show()