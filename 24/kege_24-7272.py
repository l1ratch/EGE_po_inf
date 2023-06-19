f = open('file/24_7272.txt').readline().replace('AB', "!").replace("CB", "!")

c = max_s = 0
for i in range(0, len(f)):
    if f[i] == '!':
        c += 1
    else:
        max_s = max(max_s, c)
        c = 0
max_s = max(max_s, c)
print(max_s)
