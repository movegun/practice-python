from pyexpat import model
import openpyxl
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib as mat

mat.rcParams['font.family'] = 'Hancom Gothic'
print('시작됨')
df_10years = pd.read_excel("excels/10years.xlsx", engine="openpyxl")

# [2] 데이터 확인
#print("df_10years :", df_10years)                   #(1) 읽혔는지 확인
#print("df_2012.shape :", df_10years.shape)          #(2) 데이터프레임의 ( 행 / 열 ) 갯수 확인 (41079, 15)
#print("df_10years.count() :", df_10years.count())   #(3) 각 열마다 값이 채워져있는 행의 갯수 확인
#print("df_10years.dtypes :", df_10years.dtypes)     #(4) 각 열의 dtype 확인

# [3] 데이터 정제
df_10years.drop(['시군구','번지','본번','부번','계약년월','계약날짜'],axis='columns',inplace=True)  #(1)필요없는 컬럼 삭제
print("df_10years.dtypes :", df_10years.dtypes)
print("df_10years.describe() \n:",df_10years.describe())
df_10years.astype({'거래금액(만원)':'int64'})   #(2)
print("df_10years.dtypes :", df_10years.dtypes)
print("df_10years.describe() \n:",df_10years.describe())
df_10years = df_10years.reindex(columns=['구','동','단지명','도로명','전용면적(㎡)','계약년도','계약월','계약일','거래금액(만원)','층','건축년도','old'])
print(df_10years)
dicts_10years = df_10years.to_dict('records')

from pymongo import mongo_client
from pyparsing import col

uri = "mongodb://localhost:27017"
mgCilent = mongo_client.MongoClient(uri)
db = mgCilent["movegunDB"]
coll = db["apartment"]

coll.insert_many(dicts_10years)

# x = df_10[['전용면적(㎡)','층','건축년도','계약년월']]
# y = df_10[['거래금액(만원)']]

# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)



# from sklearn.linear_model import LinearRegression

# my_model = LinearRegression()
# my_model.fit(x_train,y_train)

# y_predict = my_model.predict(x_test)

# plt.scatter(y_test , y_predict , alpha=0.4)
# plt.xlabel('실제값')
# plt.ylabel('예측값')
# plt.show()

# print(my_model.score(x_train,y_train))