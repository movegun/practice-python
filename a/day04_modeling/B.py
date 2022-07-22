import numpy as np

arr1 = np.array([6,32,44,49,51,42,8,12,16,40,81,83,33,3,9,7,26,37,28,62,32])

x = np.percentile(arr1,75) # arr1의 백분위 중 75퍼센트되는 부분은 44이다.
print(x)

# arr1의 백분위중 85퍼센트 이하의 값들만 추출하여라!

print("85% 기준값 : ",np.percentile(arr1,85))


arr2 = arr1[arr1<np.percentile(arr1,85)]
print(arr2)
