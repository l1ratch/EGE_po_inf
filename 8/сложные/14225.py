from itertools import product
c = 0
for i in product("ABCDEXYZ", repeat=4):
    w = ''.join(i)
    if w[0] in 'XZ' and w[1] in 'XZ' and w[2] in 'ABCDE' and w[3] in 'ABCDE':
        c += 1
        print(i)
print(c)
