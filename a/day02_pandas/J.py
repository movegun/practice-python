import pandas as pd

#읽기
df = pd.read_csv('자료실/dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])         # Date 컬럼 의 포멧을 날짜포멧으로 변경
#print(df.to_string())

'''df.dropna(subset=['Date'],inplace=True)         # 컬럼을 지정해서 Na(NaT, NaN ,---) 값 제거 ㅡㅡ 22번 row 사라짐
print(df.to_string())

df.loc[7,'Duration'] = 60
#df.iloc[7,0] = 60   #loc은 컬럼명 지정 iloc은 컬럼을 인덱싱
print(df.to_string())

#for문  이용해서 한번에 바꾸기

print(df.index)

for x in df.index:
    if df.loc[x,'Duration']>100:
        df.loc[x,'Duration']=100

print(df.to_string)'''


# for문 이용해서 특이값 drop해버리기

for x in df.index:
    if df.loc[x,'Duration'] >100:
        df.drop(x,inplace=True)

print(df.to_string())