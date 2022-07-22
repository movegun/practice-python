import pandas as pd

#읽기

df = pd.read_csv('자료실/data.csv')

#확인

#print(df)                   # 1. 앞5 뒤 5 확인
#print(df.to_string())       # 2. 전부다 출력 했는데 NaN 값있음 >>> 잘못된 데이터다. 마지막번호 168  

df2 = df.dropna()           # 해당 row 전체가 사라짐 배정받은 index는 그대로 작업한 결과를 df2로 >> df는 안바뀜 재료일뿐
#print(df2.to_string())

df.dropna(inplace=True)       #원본 df를 작업
print(df.to_string())

