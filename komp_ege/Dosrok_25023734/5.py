for i in range(1000):
    x = n = bin(i)[2:]
    if i % 3 == 0:
        n = n + n[-3:]
    else:
        n = n + bin(3 * (i % 3))[2:]
    r = int(n, 2)
    if r < 100:
        print(i, r)