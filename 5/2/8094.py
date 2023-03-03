for i in range(2, 10000):
    n = bin(i)[2:]
    n += str(n.count("1") % 2)
    n += str(n.count("1") % 2)
    if int(n, 2) > 43:
        print(int(n, 2))
        break