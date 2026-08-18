n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("\n")

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("\n")

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
print("\n")

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
print("\n")

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
print("\n")

n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()

print("\n")

n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()

print("\n")

def greet():
    print("Hello world")
greet()

def add_nums(num1,num2):
    sum=num1+num2
    print("Sum: ",sum)
add_nums(8,4)

def sub_nums(num1,num2):
    sub=num1-num2
    print("Sub: ",sub)
sub_nums(7,2)

def mult_nums(n1,n2):
    mult=n1*n2
    print("Mult: ",mult)
mult_nums(8,3)

def divi_nums(n1,n2):
    divi=n1//n2
    print("Divi: ",divi)
divi_nums(86,2)

def find_vowels(text):
    v=0
    vowels="aeiouAEIOU"
    for i in text:
        if i in vowels:
            v+=1
    return v
Strings="AmrutaVijayChavan"
result=find_vowels(Strings)
print("Count of vowels is: ",result)
        
