import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
x_train,x_test,y_train,y_test = train_test_split(iris['data'],iris['target'],random_state=0)

iris_dataframe = pd.DataFrame(x_train,columns=iris.feature_names)
grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train,alpha=.8,figsize=(10,10),marker='0',hist_kwds={'bins':20})
plt.show()