import numpy as np

arr1= np.array([1,2]) # 1차원
arr2= np.array([3,4]) # 1차원
print("arr1 =",arr1)
print("arr2 =",arr2)
print("---------------")
#같은 차원으로 쭊쭊
arr3 = np.concatenate((arr1,arr2))
print("arr3 = ",arr3) # 1차원
print("---------------")
arr31 = np.stack((arr1,arr2))
print("arr31 = \n",arr31) # 2차원
print("---------------")
arr32 = np.hstack((arr1,arr2))
print("arr32 = ",arr32) # 1차원
print("---------------")
arr33 = np.vstack((arr1,arr2))
print("arr33 = \n",arr33) # 2차원