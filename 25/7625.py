for i in range(211, 10**8, 211):
    if str(i)[0:2] == '11' and str(i)[4] == '4' and str(i)[-2:] == '56':
        print(i, i//211)