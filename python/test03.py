import matplotlib.pyplot as plt
import numpy as np
from statistics import linear_regression

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()

x = np.arange(1,11)
x = x.reshape(-1,1)
y = [7,9,11,13,15,17,19,21,23,25]

lr_model.fit(x,y)
a = lr_model.coef_
b = lr_model.intercept_
print(a)
print(b)
