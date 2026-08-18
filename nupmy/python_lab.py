import numpy as np
print("Creating arrays")
a= np.array([1,2,3])
print(a)


print("Zeros and Ones")
print(np.zeros((2,3)))
print(np.ones((2,2)))

print("Range Function")
print(np.arange(0,10,2))
print(np.linspace(0,1,5))

print("Random Numbers")
print(np.random.rand(3))
print(np.random.randint(1,10,5))

print("Array Shape and Reshape")
a=np.array([1,2,3,4])
print(a.shape)

b=a.reshape(2,2)
print(b)

print("Mathematical Operations")
a=np.array([1,2,3])
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

print("Element wise Operations")
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)

print("Sorting")
a=np.array([3,2,5,1])
print(np.sort(a))

print("Indexing & Slicing")
a=np.array([10,20,30,40])
print(a[1:3])

print("Matrix Operations")
a=np.array([[1,2],[3,4]])
b=np.array([[5,6,],[7,8]])
print(np.array(a))
print(np.array(b))

print("Unique Element")
a=np.array([1,2,2,3,3,4,2])
print(np.unique(a))

print("Transopose")
a=np.array([[1,2],[3,4]])
print(a.T)
