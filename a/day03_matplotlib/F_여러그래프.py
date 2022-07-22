import matplotlib.pyplot as plt
import numpy as np


yp1 = np.array([2,8,1,9,5,7])
yp2 = np.array([1,9,2,8,3,5])

plt.subplot(1,2,1)                  #1행2열 중 1번에서 작업을 하겠다.
plt.title("TITLE11111111")
plt.plot(yp1)

    
plt.subplot(1,2,2)                  #1행2열 중 2번
plt.plot(yp2)
plt.title("TITLE 22222222")



plt.suptitle("this is suptitle")
plt.show()




#https://codetorial.net/matplotlib/subplot.html