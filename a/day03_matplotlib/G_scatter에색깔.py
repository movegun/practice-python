
import matplotlib.pyplot as plt
import numpy as np


xp1 = np.array([60,60,60,45,45,60,60,45,30])
yp1 = np.array([409.1,479,340,282.4,406,300.5,374,253.3,195.1])

xp2 = np.array([10,20,30,40,50,70,60,80,90])
yp2 = np.array([409.1,479,340,282.4,406,300.5,374,253.3,195.1])

# 점 마다 색깔넣기 전체 / 각각

# 직접 지정
#plt.scatter(xp1,yp1,color='r')
#plt.scatter(xp2,yp2,color='b')

#plt.scatter(xp1,yp1,c='r')
plt.scatter(xp2,yp2,c='b')

# colors라는 배열을 만들어서 지정
#colors = np.array(['Black','Red','Green','Yellow','Blue','Magenta','Cyan','LightGray','DarkGray'])

#plt.scatter(xp1,yp1,c=colors)

# 있는 배열 사용 해당 cmap의 인덱스만 내가 지정

idx = np.array([10,20,30,40,50,60,70,80,90])
plt.scatter(xp2,yp2,c=idx,cmap='viridis')

# size

sizes = np.array([10,60,80,90,700,500,600,302,40])
plt.scatter(xp2,yp2,c=idx,cmap='viridis',s=sizes)

# alpha 투명도 alpha=0 투명 alpha=1 불투명
plt.scatter(xp2,yp2,c=idx,cmap='viridis',s=sizes,alpha=0.5)

#plt에 colorbar 추가
 
plt.colorbar()

plt.show()