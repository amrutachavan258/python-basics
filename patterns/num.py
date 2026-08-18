n=5
p=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(p,end=" ")
    p+=1
    print()

print("\n")
p=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(p,end=" ")
        p+=1
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j%2+1  if False else j%2 ,end=" ")
    print()

for i in range(1,n+1):
    for j in range(n - i):
        print(" ",end=" ")
    for j in range(2 *i-1):
        print(i, end=" ")
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(i, end=" ")
    print()
