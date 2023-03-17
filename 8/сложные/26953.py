from itertools import permutations
c = 0
for i in permutations('01234567', 5):
    if i[0] != '0':
        f = 1
        for j in range(0, len(i)-1):
            if (int(i[j]) % 2 == 0 and int(i[j+1]) % 2 == 0) or (int(i[j]) % 2 != 0 and int(i[j+1]) % 2 != 0):
                f = 0
                break
        if f == 1:
            print(i)
            c += 1
print(c)