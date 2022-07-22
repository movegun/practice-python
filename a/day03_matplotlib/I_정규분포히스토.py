import numpy as np
from numpy import random as r
import matplotlib.pyplot as plt

# x = r.normal(size=(2,3))
# x = r.normal(size=1000)

x = r.normal(0,1,100000000)

plt.hist(x)

plt.show()