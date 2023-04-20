# 15
c = 0
for A in range(200, 1, -1):
    f = 1
    for x in range(500):
        for y in range(500):
            if not(((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5))):
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        c += 1
print(c)
