import numpy as np
import math
x, y = np.array([1,3,9]), np.array([2,9,10])
mean_x = np.mean(x)
mean_y = np.mean(y)
x_error = x - mean_x
y_error = y-mean_y

rp = np.sum(x_error * y_error) /(math.sqrt(np.sum((x_error**2))) *math.sqrt(np.sum((x_error**2))))
b1 = rp*(np.std(y)/np.std(x))
b0 = y[0]-(b1*x[0])
print(b1,b0)