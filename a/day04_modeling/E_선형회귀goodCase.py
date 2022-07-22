# 선형회귀 : Good fit

import numpy as np
import matplotlib.pyplot as plt

from scipy import stats as st

x = [6,8,9,8,3,18,3,10,5,12,13,10,7]
y = [100,87,88,89,112,87,104,88,95,79,78,86,87]

plt.scatter(x,y)
plt.show()

slope, intercept , r , p , std_err = st.linregress(x,y)

print("slope:",slope)
print("intercept :",intercept)
print("r :",r)
print("p-value 유의확률 :",p)
print("std_err :" , std_err)

def myfunc(x):
    return slope*x + intercept

xymodel = list(map(myfunc,x))
print("xymodel : ",xymodel)

plt.plot(x,xymodel)
plt.show()


# 예측을 해보자

pre_Val = myfunc(11)
print("pre_Val:",pre_Val)