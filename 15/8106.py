for A in range(200):
    f = 1
    for x in range(300):
        if ((x & 29 != 0) <= ((x & 12 == 0) <= (x & A != 0))) == 0:
            f = 0
            break
    if f == 1:
        print(A)
        break