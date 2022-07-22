from re import X
import numpy

# (1) Standard Deviation

arr1 = [87,88,89,87,88,86,87]
s1 = numpy.std(arr1) # s = 표준편차
print("s1",s1)


arr2 = [33,112,139,29,60,78,98]
s2 = numpy.std(arr2)
print("s2",s2)


# (2) Variance

v1 = numpy.var(arr1)
print("v1 :",v1)

v2 = numpy.var(arr2)
print("v2 :",v2)
