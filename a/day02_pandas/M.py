import pandas as pd                   

#읽기 
df = pd.read_csv('자료실/data.csv')    

df.corr() #Correlations : 상관계수 조회
print(df.corr())