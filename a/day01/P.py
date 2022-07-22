from numpy import random as r

arr1 = [1,2,3,4]
arr2 = [ 0.2 , 0.3 , 0.5 , 0.0 ]

x1 = r.choice(arr1,p=arr2,size=100)
print("x1 = \n",x1)

x2 = r.choice(arr1,p=arr2,size=(3,5))
print("x2 = \n",x2)


arr3 = [1,2,3]
arr4 = [1/3,1/3,1/3]

x3 = r.choice(arr3,p=arr4,size=10)
print(x3)