import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = [True,True,False,True,False]

arr3 = arr1[arr2]
print(arr3)

arr31 = arr1>2
print(arr31) # [False False  True  True  True] arr1의 각각의 요소를 >2 비교 하여 T of F 반환

print(arr31.base)

arr32 = arr1[arr31]

print(arr32)


