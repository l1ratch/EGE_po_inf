f = open('files/17_7267.txt')
f = list(map(int, f))
c = 0
max_s = -10**10
min_s = min(f)
for i in range(0, len(f)-1):
    if (f[i] % 117 == min_s) or (f[i+1] % 117 == min_s):
        c += 1
        if f[i] + f[i+1] > max_s:
            max_s = f[i] + f[i+1]
    print(c, max_s)
