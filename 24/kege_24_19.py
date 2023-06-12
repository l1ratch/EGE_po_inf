f = open('file/24_7624.txt').readline()
f = f.replace('X', '.').replace('Y', '.').replace('Z', '.')
f = f.split('..')
print(f)
max_s = 0
for i in range(0, len(f)):
    if len(f[i]) > max_s:
        max_s = len(f[i])
print(max_s+2)