minn = 10**20
for i in range(64, 500):
    n = bin(i)[2:]
    n2 = n
    if n.count("1") % 2:
        n3 = n[-5:-1]
        n3 = n3.replace("1", "2").replace("0", "1").replace("2", "0")
        n = n[:-5] + n3 + n[-1]
    else:
        n3 = n[-4:].replace("1", "2").replace("0", "1").replace("2", "0")
        n = n[:-4] + n3
    r = int(n, 2)
    if r < minn:
        minn = r
        save_n = i
print(save_n)
