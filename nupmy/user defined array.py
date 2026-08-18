import array
values=array.array('i',[])
n=int(input("Enter the no of elements in the array:"))
print("Enter the element:")
for _ in range(n):
    element=int(input())
    values.append(element)
print("Original array:", values)
