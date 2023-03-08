import itertools
c = 0
for i in itertools.product('ЗИМА', repeat=5):
    if (i.count('И') == 1 and i.count('А') == 0) or (i.count('И') == 0 and i.count('А') == 1):
        c += 1
        print(i)
print(c)
