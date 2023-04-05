f = open('files/46975.txt').readlines()
f = list(map(int, f))
m = []
s = 0
max_s = -20**20
for i in range(len(f)):
    if f[i] % 2 == 0:
        m.append(f[i])
s_ar = sum(m) // len(m)
print('deb_1:', s_ar)
for i in range(len(f) - 1):
    if ((f[i] % 3 == 0) and (f[i+1] < s_ar)) or ((f[i+1] % 3 == 0) and (f[i] < s_ar)):
        s += 1
        if f[i] + f[i+1] > max_s:
            max_s = f[i] + f[i+1]
print('Ответ:', s, max_s)