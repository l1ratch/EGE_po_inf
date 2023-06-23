for i in range(1000):
    n = k = bin(i)[2:]
    if n.count("1") % 2:
        n = n + bin(n.count('1')*1)[2:]
    else:
        n = '1' + n + '00'
    r = int(n, 2)
    if r > 190:
        print(i)
        break
