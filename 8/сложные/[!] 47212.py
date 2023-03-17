# https://inf-ege.sdamgia.ru/problem?id=47212

from itertools import permutations
c = 0
for i in permutations('01234567', 5):
    if i.count('6') == 1 and c == 0:
        print('ДОДЕЛАЙ ЗАДАЧКУ')