import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal( 5.0 , 1.0 , 100000)

print(x)
plt.hist(x)
plt.show()



#정규분포와 N(0,1)인 표준정규분포 개념 이해해두기