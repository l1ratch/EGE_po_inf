for i in range(2023, 10**10, 2023):
    if str(i)[0] == '1' and str(i)[2:6] == '2139' and str(i)[-1] == '4':
        print(i, i//2023)
