import matplotlib.pyplot as plt
import numpy as np

xp = np.array([1,3,5,7])
yp = np.array([2,9,1,10])

## (1,2) / (3,9) / (5,1) / (7,10) 으로 조합

plt.plot(xp,yp,'o')
plt.show()

plt.plot(xp,'o')
plt.show()