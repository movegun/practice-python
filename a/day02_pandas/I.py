import pandas as pd

# 읽기                                  # 결측값 처리
df = pd.read_csv('자료실/data.csv')

# 확인

#print(df.to_string())


# NaN값들 채우기

#df.fillna(200,inplace=True)
#print(df.to_string)


# 특정 컬럼 지정 가능

#df['Calories'].fillna(200,inplace=True)

x = df['Calories'].median()

print(x)

#df['Calories'].fillna(x,inplace=True)

print(df.to_string())

#https://ybworld.tistory.com/54