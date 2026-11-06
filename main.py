import numpy as np
import matplotlib.pyplot as plt
from functions import mean_squared_error

x = [1,2,3,4,5,6,7,8,9,10]
y_true = [10,25,31,39,42,55,60,77,81,99]
m = 2  # slope
b = 5  # intercept
# Formula: y = b + mx

y_pred = []

for value in range(len(x)):
    predicted_value = b + m * x[value]
    y_pred.append(predicted_value)

mean_squared_error(y_true, y_pred)

"""plt.scatter(x,y_true)
plt.plot(x, y_pred)
plt.ylabel('Predicted Values')
plt.axis((0, 11, 0, 110))
plt.show()"""