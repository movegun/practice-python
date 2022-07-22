import numpy as np

arr= np.array([[1,2,3],[4,5,6]])

print("arr.shape =",arr.shape)

arr2 = np.array([1,2,3,4,5],ndmin=3)
print("arr2 =",arr2)
print("arr2.shape =",arr2.shape)