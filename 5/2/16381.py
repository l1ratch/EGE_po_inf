for i in range(2, 1000000):
    n = bin(i)[2:]
    n = n[:-1]
    if i % 2:
        n = n + "10"
    else:
        n = n + "01"
    if (int(n, 2)) == 2018:
        print(i)
        break