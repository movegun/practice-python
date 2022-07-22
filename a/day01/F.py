import numpy as np

arr = np.array([1,2,3,4,5])
print("arr.dtype = ",arr.dtype)

arr2 = np.array(["tiger","lion","rabbit"])
print("arr2.dtype = ",arr2.dtype)

arr3 = np.array([1,2,3,4,5],dtype='S') # b = binary
print("arr3 = ",arr3)
print("arr3.dtype = ",arr3.dtype)

arr4 = np.array([1,2,3,4,5],dtype='i8')
print("arr4 = ",arr4)
print("arr4.dtype = ",arr4.dtype)

arr5 = np.array([1.3,2.5,3.9])
print("arr5 = ",arr5)
arr51 = arr5.astype('i') # 같다 arr51 = arr5.astype(int)
print("arr51 = ",arr51)
print("arr51.dtype = ",arr51.dtype)

arr6 = np.array([-2,0,1,5])     # int 형 bool 로 변환 하면 0만 False 나머지 Ture
arr61 = arr6.astype(bool)
print("arr61 = ",arr61)
print("arr61.dtype() = ",arr61.dtype)