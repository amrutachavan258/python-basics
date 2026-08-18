def prime_num(number):
    if number<=1:
        return"Not prime"
    for i in range(2, int(number**0.5)+1):
        if number%i==0:
            return"Not prime"
    return"Prime"
num=int(input("Enter a number"))
print(prime_num(num))
