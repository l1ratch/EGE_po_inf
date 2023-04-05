f = open("file/27421.txt").read()
k = m = 1
for i in range(0, len(f)-1):
    if f[i] != f[i+1]:
        k += 1
    else:
        m = max(m,k)
        k = 1
print(m)