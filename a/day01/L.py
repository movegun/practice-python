import numpy as np

arr1 = np.array([1,2,3,4,5,6])

arr2 = np.array_split(arr1,3)
print("arr2 =",arr2)
print("arr2[0] =",arr2[0])
print("arr2[1] =",arr2[1])
print("arr2[2] =",arr2[2])

print("----------------------")

arr3 = np.array_split(arr1,4)
print("arr3 =",arr3)

print("----------------------")
arr4 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print("arr4 = \n",arr4)

arr41 = np.array_split(arr4,3)
print("arr41 = \n",arr41)

arr42 = np.vsplit(arr4,3)
print("arr42 = \n",arr42)