from itertools import permutations
c = 0
for i in permutations('ОЛЬГА', 5):
    w = ''.join(i)
    if i[0] != 'Ь' and not('ОЬ' in w) and not('АЬ' in w):
        c += 1
        print(i)
print(c)