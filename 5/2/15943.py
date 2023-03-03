for i in range(2, 1000):
    n = bin(i)[2:]
    n = n + n[len(n)-1]
    n = n + str(n.count("1") % 2)
    if int(n, 2) >105:
        print(int(n, 2))
        break