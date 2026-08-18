import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
transposed_arr=np.transpose(arr)
print("Original array:")
print(arr)
print("Transposed array:")
print(transposed_arr)
#reshaping array
print("reshaping array:")
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
newarrr=arr.reshape(2,3,2)
print(newarrr)

#mean and median
num=[1,2,3,4,5,6,7,8,9]
x=numpy.mean(num)
print(x)
y=numpy.median(num)
print(y)
