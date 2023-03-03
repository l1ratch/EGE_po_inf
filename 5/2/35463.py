for i in range(100, 1000):
    n = bin(i)[2:]
    s = n
    n = str(n)
    for b in range(3):
        if n.count("1") == n.count("0"):
            n += n[-1]
            print(s, n)
        elif n.count("1") > n.count("0"):
            n += "0"
        else:
            n += "1"
    r = int(n, 2)
    if r % 4 == 0:
        print(i)
        break