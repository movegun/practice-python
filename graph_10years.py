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

df_10years.drop(['시군구','번지','본번','부번','계약년월','계약날짜'],axis='columns',inplace=True)  #(1)필요없는 컬럼 삭제
df_10years.astype({'거래금액(만원)':'int64'})   #(2)
df_10years = df_10years.reindex(columns=['구','동','단지명','도로명','전용면적(㎡)','계약년도','계약월','계약일','거래금액(만원)','층','건축년도','old'])

#   연도 - 거래량
df = df_10years.groupby('계약년도').count().reset_index()
#df = df.reset_index()
#df = df.rename(columns={'':'거래량'})
df.plot(kind='bar',x='계약년도',y='층')
plt.show()
