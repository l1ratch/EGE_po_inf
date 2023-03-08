from itertools import permutations
c = 0
for i in permutations('ЛЕВИЙ',5):
    w = ''.join(i)
    if i[0] != 'Й' and not('ЕИ' in w):
        c += 1
print(c)