from itertools import product
c = 0
for i in product("ABCDXYZ", repeat=4):
    w = ''.join(i)
    if i[0] == 'X' or i[0] == 'Y' or i[0] == 'Z':
        if w[1:].find('X') == -1 and w[1:].find('Y') == -1 and w[1:].find('Z') == -1:
            c += 1
print(c)