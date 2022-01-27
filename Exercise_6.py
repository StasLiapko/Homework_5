x = list(map(int, (input("Input number"))))
y = []
for i in x[::]:
    y =+ (i*2)
    x.append(y)
print(x)
