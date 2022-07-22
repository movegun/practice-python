from numpy import random as r
import numpy as np

arr1 = [1,2,3,4]
arr2 = np.array(arr1)

print(arr2)
r.shuffle(arr2)         ## arr2를 변경시켜버림 return값 없음!!! print 불가
print(arr2)

arr3 = np.array(arr1)
r.permutation(arr3)     #arr3를 근본적 변경은 아니고 섞인 값을 리턴해줌

print(r.permutation(arr3))
print(arr3)             #다시 찍어도 안바뀌어있음