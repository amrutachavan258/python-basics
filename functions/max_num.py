def find_max(num1,num2):
    return num1 if num1>num2 else num2
a=int(input("Enter first num: "))
b=int(input("Enter second num: "))

print("Maximum:",find_max(a,b))
