f = open("files/37341.txt").readlines()
f = list(map(int, f))
c = m = 0
max_s = -10**10
for i in range(0, len(f)-1):
    for k in range(i + 1, len(f)):
        if ((f[i] - f[k]) % 2 == 0) and ((f[i] % 19 == 0) or (f[k] % 19 == 0)):
            c += 1
            if f[i] + f[k] > max_s:
                max_s = f[i] + f[k]
                m = max(m, f[i] + f[k])
print(c, m)