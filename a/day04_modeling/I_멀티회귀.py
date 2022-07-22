# 멀티회귀

import pandas as pd
from sklearn import linear_model # scipy의 liner랑 다른 liner.regress 사용하기위해

df = pd.read_csv("C:\LDG\PyAdvanced\day04\자료실\cars1.csv")
#print(df.head(10))

X = df[['Weight','Volume']]
#print(X)

y = df[['CO2']]
#print(y)

lr = linear_model.LinearRegression()
lr.fit(X,y)

print("lr.predict([[1500,2000]]) :",lr.predict([[1500,2000]]))

print("lr.coef_ : ", lr.coef_)

print("lr.predict([[1500,5000]]) :",lr.predict([[1500,5000]]))