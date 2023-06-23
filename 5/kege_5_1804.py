for i in range(0, 100000):
    n = bin(i)[2:]
    n = str(n) + str((n.count('1')*1) % 2)
    n = str(n) + str((n.count('1')*1) % 2)
    r = int(n, 2)
    if r > 249:
        print(i)
        break