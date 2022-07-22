from numpy import random as r



x1 = r.randint(100)
print("x1 = ",x1)

x2 = r.rand() # 0~1 사이의 실수
print("x2 = ",x2)

x3 = r.randint(100,size=5) # 길이 5 인 1차원 배열
print("x3 = ",x3)

x4 = r.randint(100,size=(3,5)) # (3,5)의 2차원배열
print("x4 = \n",x4)

x5 = r.rand(5) # 0~1 사이의 실수 5개인 1차원배열        = r.rand(1,5)
print("x5 = ",x5)

x6 = r.rand(3,5)
print("x6 = ",x6)

x7 = r.choice([1,2,3,4])
print("x7 = ",x7)

x8 = r.choice((1,2,3,4),size=(3,4))
print("x8 = \n",x8)