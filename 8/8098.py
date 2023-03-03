from itertools import product
s = 0
for i in product("СЛОН", repeat=5):
    if i.count("С") == 1:
        s += 1
print(s)