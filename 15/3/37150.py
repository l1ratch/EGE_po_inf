for A in range(200):
    f = 1
    for x in range(500):
        for y in range(500):
            if ((2*x + y != 70) or (x < y) or (A < x)) == 1:
                f = 0
                break