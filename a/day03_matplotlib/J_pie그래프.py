
import matplotlib.pyplot as plt
import numpy as np

yp = np.array([30,20,40,10])


#plt.pie(yp)                 # 기본방향>> 3시방향에서 counterclockwise(반시계)로


#   시작방향 + 라벨이름 + 강조 + 색깔 + 음영

nameOflabels = ['A','B','C','D']
levelOfexplode = [0.1 , 0.2 , 0.3 , 0.4]
ccolors = ['r','b','y','r']

plt.pie(yp , labels=nameOflabels , startangle=90 , explode=levelOfexplode , colors=ccolors ,shadow=True)    



# 색깔 설명 (legend)


#plt.legend()
plt.legend(title='this is legend\'s title')


plt.show() 