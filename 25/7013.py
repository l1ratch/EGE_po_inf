for x in range(-1, 10**4):
    for y in range(-1, 10**4):
        n = (str(x) + '31' + str(y) + '65').replace('-1', '')
        if ((int(n) % 31) == 0) and ((int(n) % 2031) == 0) and (int(n) < 10**9):





