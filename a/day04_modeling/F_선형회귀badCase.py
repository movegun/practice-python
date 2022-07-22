
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = [90,44,37,37,96,11,67,35,39,21,27,30,49,65,7,6,37,67,73,41]
y = [22,47,4,36,68,96,54,73,59,11,27,35,91,34,39,21,57,3,48,16]

plt.scatter(x,y)
#plt.show()

print(stats.linregress(x,y))
slope, intercept, r , p , std_err = stats.linregress(x,y)

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
