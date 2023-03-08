from itertools import permutations
c = 0
for i in permutations('ГЕРАСИМ',7):
    w = ''.join(i)
    f = 1
    for e in range(6):
        if (i[e] in 'ГРСМ' and i[e + 1] in 'ГРСМ') or (i[e] in 'ЕАИ' and i[e + 1] in 'ЕАИ'):
            f = 0
            break
    if f == 1:
        c += 1
print(c)