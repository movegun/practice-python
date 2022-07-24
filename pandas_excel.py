from pydoc import describe
import openpyxl
import pandas as pd
import numpy as np

# [1] 2012년 엑셀파일 읽기
df_2012 = pd.read_excel("excels/2012.xlsx", engine="openpyxl")

# [2] 데이터 확인
#print("df_2012 :", df_2012)                   #(1) 읽혔는지 확인
#print("df_2012.shape :", df_2012.shape)       #(2) 데이터의 ( 행 / 열 ) 갯수 확인 (41079, 15)
#print("df_2012.count() :", df_2012.count())   #(3) 각 열마다 값이 채워져있는 행의 갯수 확인
#print("df_2012.dtypes :", df_2012.dtypes)     #(4) 각 열의 dtype 확인
print("df_2012.describe() \n:",df_2012.describe())
input()
                                               #                     (3)      (4)
                                                    #시군구         41079    object
                                                    #번지           41079    object
                                                    #본번           41079    int64
                                                    #부번           41079    int64
                                                    #단지명         41079    object
                                                    #전용면적(㎡)    41079   float64
                                                    #계약년월        41079   int64
                                                    #계약일          41079   int64
                                                    #거래금액(만원)   41079  object
                                                    #층              41079   int64
                                                    #건축년도        41079   int64
                                                    #도로명          41079   object
                                                    #해제사유발생일     0    float64
                                                    #거래유형         41079  object
                                                    #중개사소재지     41079  object

# [3] 데이터 정제  
                                                  
# (1) 각 컬럼의 dtype을 알맞게 변경          계약년월/계약일/건축년도 필요하면 date타입으로 변경해야할듯
df_2012.astype({'본번':'object','부번':'object','거래금액(만원)':'int64'})
print("df_2012.dtypes :", df_2012.dtypes) 
input()
# (2) 결측값 처리
#print("df_2012[df['거래금액(만원)'].isnull()]",df_2012[df_2012['거래금액(만원)'].isnull()])

# (3) 이상값 처리                       근데 이미 완벽한 데이터프레임이라 패스 확인만 하면될듯

# (4) 필요한 컬럼만 수집
# axis=0 행 작업 // axis=1 열 작업

#df_2012 = df_2012.drop(['번지','본번','부번','도로명','해제사유발생일','거래유형','중개사소재지'],axis=1) # 필요없는 열 삭제 inplace=True 옵션 하지마셈!!!!!!!!꼬임꼬임꼬임꼬임꼬임

df2=df_2012["시군구"].value_counts().sort_index().reset_index()      #같은 값의 갯수 개포동 : 649개
print("df2:\n",df2)
input("aaaa")
print(df2.describe())

for i,item in df2['index'].iteritems():
          
     df2.loc[i,'index'] = item[0:9]
     
print("df2 :\n",df2)
input("bbbbbbbb")
print(df2.count())
df2.groupby('시군구').sum()
print(df2)

# def cut(object):
#      for i,obj in object:
#           object[i]=object[i]
     
#      pass
     

# cut(a)

'''# [4] 시각화
import matplotlib as mat
import matplotlib.pyplot as plt
mat.rcParams['font.family'] = 'Hancom Gothic'

df_day_maen = df_2012.groupby('계약일').mean()
df_floor_maen = df_2012.groupby('층').mean()
df_BuiltedDate_maen = df_2012.groupby('건축년도').mean()

#df_day_maen = df_2012.groupby('계약일').mean().reset_index()
#df_floor_maen = df_2012.groupby('층').mean().reset_index()
#df_BuiltedDate_maen = df_2012.groupby('건축년도').mean().reset_index()

print(df_day_maen["거래금액(만원)"])
print(df_floor_maen['거래금액(만원)'])
print(df_BuiltedDate_maen['거래금액(만원)'])

plt.subplot(1,2,1)
df_floor_maen['거래금액(만원)'].plot(kind = 'bar')

plt.subplot(1,2,2)
df_BuiltedDate_maen['거래금액(만원)'].plot(kind = 'line')

plt.show()'''



'''print(df_day_maen['거래금액(만원)'])
print(df_floor_maen['거래금액(만원)'])
print(df_BuiltedDate_maen['거래금액(만원)'])'''

# 우리 했던 예제 흐름 따라가면서 데이터 정제 및 시각화 하도록