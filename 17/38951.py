# 17
f = open('files/38951.txt').readlines()
f = list(map(int, f))
s = 0
m = -1
for i in range(len(f)-1):
    if ((f[i] % 3) == 0 or (f[i+1] % 3) == 0) and (f[i] + f[i + 1]) % 5 == 0:
        s += 1
        if f[i] + f[i + 1] > m:
            m = f[i] + f[i + 1]
print(s, m)
