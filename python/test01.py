import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-np.pi,np.pi, num=100,endpoint=False)
y = np.cos(x)
plt.plot(x,y)
plt.show()