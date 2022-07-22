#모델 정확도를 측정 ( Train / Test )

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)       # random 하게 생성한 seed의 2번째 모델을 사용하므로 실행할때마다 값이 안달라짐

x = np.random.normal(3,1,1000)
y = np.random.normal(200,50,1000)/x

'''print(x,y)
plt.scatter(x,y)
plt.show()'''

train_x=x[:800]
train_y=y[:800]

test_x = x[800:]
test_y = y[800:]

'''plt.scatter(train_x,train_y)
plt.show()
plt.scatter(test_x,test_y)
plt.show()'''

train = np.polyfit(train_x,train_y,4)
mymodel = np.poly1d(train)
myXs = np.linspace(0,6,1000)

plt.scatter(train_x,train_y)
plt.scatter(myXs,mymodel(myXs))
plt.show()

train_r2 = r2_score(train_y,mymodel(train_x))
print("train_r2:",train_r2)

test_r2 = r2_score(test_y,mymodel(test_x))
print("text_r2 :",test_r2)

preY = mymodel(5)
print("preY : ",preY)