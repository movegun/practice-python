import numpy as np

arrOriginal= np.array([1,2,3,4,5])

arrCopy = arrOriginal.copy() # 카피하고
arrView = arrOriginal.view() # view를 하고

arrOriginal[0] = 10     # 원본에 변화를 주면

print("arrOriginal = ", arrOriginal) # 원본 변화
print("arrCopy = ", arrCopy)         # 카피본은 안변함
print("arrView = ", arrView)         # view 는 변함 엄밀히 변하는게 아니고 변한 원본을 비춰주는것

print("arrCopy.base =",arrCopy.base)
print("arrView.base =",arrView.base)