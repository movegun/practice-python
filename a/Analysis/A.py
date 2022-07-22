import math

import numpy as np
import pandas as pd
import matplotlib

import matplotlib.pyplot as plt

import seaborn as sns
plt.style.use("seaborn")
sns.set( font_scale = 1 )
sns.set_style('whitegrid')

import plotly.express as px

import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)

import plotly.graph_objects as go
import plotly.offline as pyo
#pyo.init_notebook_mode() # 주피터 ? 

from plotly.subplots import make_subplots

import missingno as msno

import warnings
warnings.filterwarnings(action='ignore')

matplotlib.rcParams['font.family'] = 'Hancom Gothic'

## 데이터 읽어오기
df = pd.read_csv("C:/LDG/PyAdvanced/Analysis/Data/1_서울시/(3)서울시 공공자전거 이용정보(일별)/서울특별시 공공자전거 이용정보(일별)_22.06.csv",encoding ="cp949")
#print(df.head())
## 데이터 정보 확인

#print(df.info())

##수치형 데이터 통계 확인
pd.options.display.float_format = '{:.2f}'.format
#print(df.describe())

##범주형 데이터 통계 확인

#print(df.describe(include=np.object_))

msno.bar(df)
plt.show()

## 이동거리  운동량 상관관계

f , ax = plt.subplots(1,1, figsize=(10,10))
print(f,ax)

sns.barplot(data=df,x="운동량",y="탄소량")
ax.set_xlim(-100,1000)
ax.set_title("운동 ㅡ 탄소 상관관계",size=20)

plt.show()