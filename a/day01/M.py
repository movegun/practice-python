import numpy as np

arr1 = np.array([1,2,3,4,5,3,3])
print("arr1 = ",arr1)
x = np.where(arr1==3)
print("np.where(arr1==3) = ",x)

y = np.where(arr1%2==0)
print("np.where(arr1%2==0) =",y)

z1 = np.searchsorted(arr1,3)
print("np.searchsorted(arr1,3) = ",z1)

z2 = np.searchsorted(arr1,3,side='left') # 고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민고민
print("np.searchsorted(arr1,3,side='right') = ",z2)
print("np.searchsorted(arr1,3,side='right') = ",z2)
print("np.searchsorted(arr1,3,side='right') = ",z2)
print("np.searchsorted(arr1,3,side='right') = ",z2)
print("np.searchsorted(arr1,3,side='right') = ",z2)


print("--------------------")

arr2 = np.array(['C','A','B'])
print("arr2 = ",arr2)
print("np.sort(arr2) =",np.sort(arr2))

print("--------------------")

arr3 =  np.array([True,False,True])
print("arr3 = ",arr3)
print("np.sort(arr3) = ",np.sort(arr3))

print("--------------------")

arr4 = np.array([[2,1,3],[5,4,6]])
print("arr4 = ",arr4)
print("np.sort(arr4) = ",np.sort(arr4))