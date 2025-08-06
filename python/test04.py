import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('examdata.csv')
mask = data.loc[:,'pass']==1
x = data.drop(labels=['pass'],axis=1)
y = data.loc[:'pass']

x1 = data.loc[:'exam1']
x2 = data.loc[:'exam2']

LR = LogisticRegression()
LR.fit(x.values,y)

y_predict = LR.predict(x.values)
accuracy = accuracy_score(y,y_predict)
y_test = LR.predict([[70,65]])

theta0 = LR.intercept_
theta1,theta2 = LR.coef_[0][0],LR.coef_[0][1]

x2_new = -(theta0+theta1 * x1)/theta2

fig1 = plt.figure()
passed = plt.scatter(data.loc[:,'exam1'][mask],data.loc[:,'exam2'][mask])
failed = plt.scatter(data.loc[:,'exam1'][~mask],data.loc[:,'exam2'][~mask])
plt.plot(x1,x2_new)

plt.legend((passed,failed),('passed','failed'))
plt.title('exam1_exam2')
plt.xlabel('exam1')
plt.ylabel('exam2')

plt.show()