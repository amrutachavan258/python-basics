import numpy as np
#1-D
arr=np.array([1,2,3,4,5,6])
print(arr)
print(arr[1:4])
print(arr[1:])
print(arr[:5])
print(arr[-3:-1])
print(arr[1:5:2 ])
#2-D
#row slicing
arr1=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr1[1,2:5])

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,2])
