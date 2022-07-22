import matplotlib.pyplot as plt
import numpy as np



xp = np.array([60,60,60,45,45,60,60,45,30])
yp = np.array([409.1,479,340,282.4,406,300.5,374,253.3,195.1])

plt.plot(xp,yp)


font1 = {'family':'Arial Black', 'color':'red','size':18}
font2 = {'family':'Consolas', 'color':'green','size':20}


plt.xlabel("Duration")
plt.ylabel("Carl")
plt.title("< Dur and Cal >",fontdict=font2,loc='center')

#plt.grid(axis='x')
#plt.grid(axis='y')
plt.grid(True, axis='y', color='red', alpha=0.5, linestyle='--')

plt.show()


#https://wikidocs.net/92089 https://wikidocs.net/92089https://wikidocs.net/92089https://wikidocs.net/92089https://wikidocs.net/92089https://wikidocs.net/92089