from itertools import product
c = 0
for i in product("ЕГЭ", repeat=5):
    if i[0] == "Е" or i[0] == "Э":
        c += 1
print(c)
