for i in range(10000, 5, -1):
    s = bin(i)[2:]
    s = s + str(s.count("1") % 2)
    s = s + str(s.count("1") % 2)
    r = int(s, 2)
    if r < 90:
        print(r)
        break

