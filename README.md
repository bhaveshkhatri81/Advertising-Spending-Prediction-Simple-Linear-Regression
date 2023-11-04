## Explanation:
I created these scripts to solve an exponential equation for the data inside `.\Data set\CO2-by-source.xlsx`.

The script uses linear regression to compute for the coefficients a, b, and c. The script will optimize the values so it can result in a smaller error.


**Please check out the actual python script for detailed explanation on the regression analysis model. Please Please**
## Set-up:
Python version: 3.11.3
Installed packages:
```
Package           Version
----------------- -------
contourpy         1.0.7
cycler            0.11.0
et-xmlfile        1.1.0
fonttools         4.39.4
kiwisolver        1.4.4
matplotlib        3.7.1
metaplot          1.1.0
numpy             1.24.3
openpyxl          3.1.2
packaging         23.1
pandas            2.0.1
Pillow            9.5.0
Pint              0.22
pip               23.1.2
pyparsing         3.0.9
python-dateutil   2.8.2
pytz              2023.3
scipy             1.10.1
setuptools        65.5.0
six               1.16.0
typing_extensions 4.6.2
tzdata            2023.3
```

## Step by step set-up:
1. Install python on your computer
2. Copy and paste this repository into a new folder.
3. It is recommanded to set up a virtual environment in the folder before running the python command.
4. Run the command ```python -m venv .env ``` to make a python environmnt.
5. Run the command ```pip install -r requirements.txt``` to install all the required packages for this project.
6. Run the command ```python.exe analyze_data.py.py``` to run the analysis.

## Summary of the files:
1. **analyze_data.py**: The main python script that runs the analysis.
2. **CO2-by-source.xlsx**: The training data for the model
3. **verification.py**: The python script that verifies the model with the training data.
4. **regression_analysis.py**: The python script that contains the regression analysis model.
5. **requirements.txt**: The file that contains all the required packages for this project. 


## References:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

https://scipy-cookbook.readthedocs.io/items/robust_regression.html