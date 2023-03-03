a = []
for i in range(10, 1001):
    n = bin(i)[2:]
    n = n[1:]
    n = int(n, 2)
    if i - n not in a:
        a.append(i - n)
print(len(a))
