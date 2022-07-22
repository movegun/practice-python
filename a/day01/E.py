import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
'''
print("arr = ", arr)
print("-----------------------------")
print("arr[1:3] =", arr[1:3])

print("arr[-3:-1] =", arr[-3:-1])

print("arr[1:10:2] =", arr[1:10:2]) # step = 2

print("arr[::2] = " , arr[::2])     # 전부다 , step = 2
'''
print("-----------------------------")

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print("arr2 = \n",arr2)
print("-----------------------------")
print("arr2[1,1:3] = ",arr2[1,1:3]) # 1번째 배열의 1이상 3미만
print("arr2[0:2,2] = ",arr2[0:2,2]) # 모든 배열의 2인덱스 컬럼
print("arr2[0:2,1:3] = \n",arr2[0:2,1:3]) # 모든 배열의 1이상 3미만 컬럼


print(arr.ndim)
print(arr2.ndim)

