from turtle import color
import matplotlib.pyplot as plt
import numpy as np

xp = np.array(["A","B","C","D"])
yp = np.array([20,80,50,70])

#세로막대
#plt.bar(xp,yp)

#가로막대
#plt.barh(xp,yp)

#꾸미기
plt.bar(xp,yp,color='r',width=0.1)          #세로막대는 폭을 width로 조정
plt.barh(xp,yp,color='b',height=0.2)        #가로막대는 폭을 height로 조정



plt.show()