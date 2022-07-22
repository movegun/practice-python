import numpy as np

arr= np.array([1,2,3,4,5,6,7,8,9,10])

for a in arr:
    print(a)
print("----------------")
arr2 = np.array([[1,2],[3,4]])

for a in arr2:
    print(a)
print("----------------")    
for a in arr2:
    for aa in a :
        print(aa)
print("----------------")

arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for a in arr3:
    for aa in a:
        for aaa in aa:
            print(aaa)
            print("-")

print("----------------")

for a in np.nditer(arr3):
    print (a)

print("----------------")

arr4 = np.array([1,2,3,4,5])

for idx , a in np.ndenumerate(arr4):
    print(idx,a)
    
print("----------------")

arr5 = np.array([[1,2],[3,4]])
print("arr5 = \n",arr5)
print("----------------")
for idx , a in np.ndenumerate(arr5):
    print(idx,a)