import numpy as np

arr= np.array([1,2,3,4,5,6,7,8,9,10])

print("arr.shape = ",arr.shape)
arr2 = arr.reshape(2,5)
print(arr2)

arr3= np.array([1,2,3,4,5,6,7,8,9,10,11,22])

arr31 = arr3.reshape(4,3)
print("arr31 = \n",arr31)

arr32 = arr3.reshape(2,3,2)
print("arr32 = \n",arr32)
print(arr32[0,0,1])

arr3[5]=35
print("arr32 = \n",arr32) # reshape 은 shape을 바꾼 후 view 라고 이해



arr4 = np.array([[1,2],[3,4]])
arr41 = arr4.reshape(-1)
print("arr41 = ",arr41)

arr5 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr51 = arr5.reshape(-1)
print("arr51 = ",arr51)
