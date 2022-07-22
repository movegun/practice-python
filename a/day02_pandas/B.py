import pandas as pd

a = [5,9,3,4]

s1 = pd.Series(a)
print(s1)
print("-------------------")
print(s1[0])

print("-------------------")

s2 = pd.Series(a,index=["x","y","z","k"])       # 인덱스를 내가 직접 설정
print(s2)
print("s2[\"z\"] : ",s2["z"])

print("-------------------")

b = {"one":170,"two":165,"three":185}           # key 값이 index가 됨

s3 = pd.Series(b)
print(s3)

print("-------------------")

s4 = pd.Series(b,index=["one","two"])
print(s4)