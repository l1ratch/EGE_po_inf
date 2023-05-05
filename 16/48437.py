def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + n


c = 0
for i in range(500):
    print(i, f(i))