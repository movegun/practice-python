import pandas as pd

# 데이터 읽어오기
df = pd.read_json('자료실/data.json')
# 확인

print(df.to_string())
#print(df['Pulse'].nunique())

#https://bigdaheta.tistory.com/43