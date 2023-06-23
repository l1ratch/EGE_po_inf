from itertools import product
s = 0
for i in product('РУСЛАН', repeat=5):
    if i.count('У') == 1 and i.count('А') == 1:
        s += 1
print(s)
