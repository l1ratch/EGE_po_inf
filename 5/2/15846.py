for i in range(2, 1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n2 = n + "00"
    else:
        n2 = n + "11"
    r = int(n2, 2)
    if r > 115:
        print(i)
        break
