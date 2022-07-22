import pandas as pd


# DataFrame : 2차원 테이블형태의 데이터 구조

a = {
    "calories" : [700,200,500],
    "duration" : [50,20,30]    
}

df = pd.DataFrame(a)
print(df)

print("------------------")

print(df.loc[1])    #index 1의 row 리턴

print("------------------")

print(df.loc[[0,2]])     # index 0과 2를 row 리턴

print("------------------")

df2 = pd.DataFrame(a,index=["d1","d2","d3"])
print("df 2 = \n ",df2)

print("------------------")

print (df2.loc[["d1","d3"]])

print(df['calories'][0])