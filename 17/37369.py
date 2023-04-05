f = open("files/37369.txt").readlines()
f = list(map(int, f))
c = m = 0
for i in range(0, len(f)-1):
    for j in range(i + 1, len(f)):
        if (f[i] - f[j]) % 80 == 0:
            c += 1
            m = max(m, abs(f[i] - f[j]))
print(c, m)