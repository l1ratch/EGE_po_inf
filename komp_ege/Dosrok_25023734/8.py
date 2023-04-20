import itertools
n = 0
for i in itertools.product("АВЛОР", repeat=4):
    n += 1
    if i[0] == "Л":
        print(n)
        break