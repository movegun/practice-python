import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [2,3,4,6,7,8,9,10,11,13,14,15,16,17,19,20,22,23]
y = [101,91,81,61,61,56,61,66,71,71,76,77,79,80,91,100,100,101]

plt.scatter(x,y)
#plt.show()

arr1 = np.polyfit(x,y,3)#3차식 계수들을 arr1에 담음

mymodel = np.poly1d(arr1)

print("mymodel \n:", mymodel)

myline = np.linspace(2,23,1000) # 2~23 사이를 1000등분한 x값들을 준비

#print("myline:",myline)

plt.plot(myline,mymodel(myline))
plt.show()

r = r2_score(y,mymodel(x))
print("r:",r) #r: 0.9432150416451025 >> 1에 가까우니까 xㅡy의 관계가 있다.

# x가 18일때 모델을 통해 결과값 y를 예측할수있나 ? 

x = 18
y = mymodel(x)
print("y(x=18일때 예측값):",y)


'''
a , b , c = np.polyfit(x,y,2)
print(np.polyfit(x,y,2))


print(len(x))
#def fun(x):
#    return ws[0]*x**2 + ws[1]*x + ws[2]

def fun(x):
    return a*x**2 + b*x + c

xymodel = list(map(fun,x))

print("xymodel : ",xymodel)

plt.plot(x,xymodel)

plt.show()'''





