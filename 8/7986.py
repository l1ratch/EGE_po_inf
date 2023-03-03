from itertools import product
s = 0
for i in product("ЗИМА", repeat=5):
    if i[0] == "З" or i[0] == "М":
        if i[-1] == "И" or i[-1] == "А":
            s += 1
print(s)