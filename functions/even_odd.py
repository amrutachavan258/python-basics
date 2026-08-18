def even_odd(num1):
    if num1%2==0:
        return"Even"
    else:
        return"Odd"
    
number=int(input("enter number: "))
print(even_odd(number))
