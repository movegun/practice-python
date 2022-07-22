import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [90,44,37,37,96,11,67,35,39,21,27,30,49,65,7,6,37,67,73,41]
y = [22,47,4,36,68,96,54,73,59,11,27,35,91,34,39,21,57,3,48,16]

plt.scatter(x,y)
#plt.show()

arr1 = np.polyfit(x,y,3)
print(arr1)

mymodel = np.poly1d(arr1)

myline = np.linspace(6,96,200)
plt.plot(myline,mymodel(myline))
plt.show()

r = r2_score(y,mymodel(x))
print("r :",r) # r : 0.009952707566680541 0에 가까우므로 xㅡy의 관계성이 적다 그러므로 모델만들기에 적합하지않다.