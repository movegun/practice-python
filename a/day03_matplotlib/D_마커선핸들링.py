import matplotlib.pyplot as plt
import numpy as np
'''
yp = np.array([2,8,1,9,5,7])


# (1) linestyle

#plt.plot(yp, linestyle="dotted")
plt.plot(yp,ls=":")

#plt.plot(yp, linestyle="dashed")
plt.plot(yp,ls="--")

#plt.plot(yp,linestyle="dash-dot")
plt.plot(yp,ls="-.")    

#plt.plot(yp,linestyle="solid")
plt.plot(yp,ls="-")

# (2) line-color

#plt.plot(yp,color="r")
#plt.plot(yp,color="#0cf0f7") #colorpicker 로 가능

# (3) line-width

plt.plot(yp,linewidth='15')'''

# (4) 여러 Lines

yp = np.array([2,8,1,9,5,7])
yp2 = np.array([4,7,2,8,6,3])

#plt.plot(yp,yp2) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

plt.plot(yp)        # O
plt.plot(yp2)       # O


plt.show()