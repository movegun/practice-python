import numpy as np

arr0= np.array(12) # 0차원
arr1 = np.array([1,2,3,4]) # 1차원
arr2 = np.array([[1,2],[3,4]]) # 2차원
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # 3차원

print("arr0",arr0)
print("arr0.ndim = ",arr0.ndim)
print("---------------------")
print("arr1 \n",arr1)
print("arr1.ndim = ",arr1.ndim)
print("---------------------")
print("arr2 \n",arr2)
print("arr2.ndim = ",arr2.ndim)
print("---------------------")
print("arr3 \n",arr3)
print("arr3.ndim = ",arr3.ndim)