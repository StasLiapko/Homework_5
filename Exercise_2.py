n = int(input("Input number"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)