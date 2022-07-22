import pandas as pd

df = pd.read_csv('./자료실/data.csv')

#print(df)
#print(df.to_string())      # header 5개 + ''' +  tailer 5개 로 표시
#print(pd.options.display.max_rows) # 참고 : 디스플레이되는 최대 row 갯수
# 먼말이냐면 밑에 터미널에 생략되어 표시되는 ''' 표시 보면 이해됨

pd.options.display.max_rows = 70 # 50개 보이게 바꾸고 프린트하면 '''을 제외하고 50개
print(df)