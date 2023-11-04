import numpy as np
import matplotlib.pyplot as plt
import regression_analysis

def piecewise_func(x, first_sector, second_sector):
    y = np.zeros_like(x)
    y[(0 <= x) & (x <= 6)] = regression_analysis.nonlinear_func(x[(0 <= x) & (x <= 6)], *first_sector)
    y[(6 < x) & (x <= 13)] = regression_analysis.nonlinear_func(x[(6 < x) & (x <= 13)], *second_sector)
    return y


# x = np.linspace(-5, 5, 1000)
# y = piecewise_func(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Piecewise Function')
# plt.show()