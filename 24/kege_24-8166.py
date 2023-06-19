f = open('file/24_8166.txt').readline().replace('A', '!').replace('B', '!').replace('C', '!')

c = 0
max_s = 0
for i in range(0, len(f)):
    if f[i] == '!':
        c += 1
    else:
        max_s = max(max_s, c)
        c = 0
max_s = max(max_s, c)
print(max_s//2)






























