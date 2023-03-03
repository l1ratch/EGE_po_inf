a = []
min_r = 1100
for i in range(1000):
    n = bin(i)[2:]
    if (n.count("1")%2==1):
        n = "11" + n[2:] + "1"
    else:
        n = "1" + n[2:] + "0"
    r = int(n, 2)
    if r > 25 and r < min_r:
        min_r = r
        n_ = i
print(min_r, n_)