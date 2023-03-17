# for A in range(200, 1, -1):
#     c = 0
#     for x in range(500):
#         for y in range(500):
#             if ((x <= 9) <= (x * x <= A)) and ((y*y <= A) <= (y <= 9)):
#                 c += 1
#     if c == 250000:
#         print(A)
#         break

for A in range(200, 1, -1):
    f = 1
    for x in range(500):
        for y in range(500):
            if not(((x <= 9) <= (x * x <= A)) and ((y*y <= A) <= (y <= 9))):
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A)
        break