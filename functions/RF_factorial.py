def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(6),"\n")

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
terms=6
print("series: ")
for i in range(1,terms+1):
    print(fibonacci(i),end=" ")

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print("\n",factorial(5))
