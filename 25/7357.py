for i in range(53191, 10**10, 53191):
    if (int(str(i)[0]) % 2 == 0) and str(i)[1:4] == '136' and (int(str(i)[4:]) % 2 != 0):
        print(i, i//53191)