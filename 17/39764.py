f = open('files/39764.txt').readlines()
f = list(map(int, f))
s = max_s = 0
for i in range(len(f)-2):
    x = sorted([f[i], f[i+1], f[i+2]])
    if x[2]**2 == (x[0]**2 + x[1]**2):
        s += 1
        max_s = max(max_s, sum(x))
print(s, '_', max_s)
