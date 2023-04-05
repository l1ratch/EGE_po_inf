f = open("files/37337.txt").readlines()
f = list(map(int, f))
c = 0
max_s = -10**10
for i in range(0, len(f) - 1):
    for j in range(i + 1, len(f)):
        if f[i] % 160 != f[j] % 160:
            if (f[i] % 7 == 0) or (f[j] % 7 == 0):
                c += 1
                if f[i] + f[j] > max_s:
                    max_s = f[i] + f[j]
print(c, max_s)
