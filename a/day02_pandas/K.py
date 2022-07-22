import pandas as pd

#읽기
df = pd.read_csv('자료실/dirtydata.csv')                    #중복 데이터 제거

#print(df.duplicated())                         #중복 데이터 True False로 조회  12번row 중복

#df.drop_duplicates(inplace=True)

print(df.to_string)

print(df.keys())