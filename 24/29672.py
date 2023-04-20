f = open('file/29672.txt')
a = 0
for s in f:
    if s.count('E') > s.count('A'):
        a += 1
print(a)
