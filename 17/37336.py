f = open('files/37336.txt').readlines()
f = list(map(int, f))
s = 0
max_s = -20**20
for i in range(len(f)-1):
    if (f[i] % 3) == 0 or (f[i+1] % 3) == 0:
        s += 1
        if f[i] + f[i + 1] > max_s:
            max_s = f[i] + f[i + 1]
print(s, max_s)