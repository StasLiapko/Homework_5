a = []
for i in range(7500,15000, 547):
    a.append(i)
    if len(a) > 11:
        break
print(a, sum(a) / len(a), sep = "\n")

