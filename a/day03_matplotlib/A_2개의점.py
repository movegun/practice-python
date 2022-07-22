import matplotlib.pyplot as plt
import numpy as np

xp = np.array([0,6])
yp = np.array([0,300])

## (0,0) / (6,300) 으로 조합


print(xp)
print(yp)

plt.plot(xp,yp)     # 선
plt.plot(xp,yp,'o') # 점


plt.show()