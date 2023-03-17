for i in range(61, 91):
    a = '1'*i
    while '111' in a:
        a = a.replace('111', '2', 1)
        a = a.replace('222', '11', 1)
    if a == '2211':
        print(i)