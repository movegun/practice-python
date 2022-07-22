import openpyxl
import pandas as pd

# 데이터 읽어오기
df1 = pd.read_excel("자료실/경기도인구데이터.xlsx", engine="openpyxl")

# 확인
print(df1)

# 엑셀로 가져온 데이터를 다른 형식의 데이터로 쓰기

#df1.to_csv("자료실/output/경기도인구데이터.csv",index=False)
#df1.to_json("자료실/output/경기도인구데이터22.json")
