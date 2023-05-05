import time

start_time = time.time()


def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return f(n / 2)


c = 0
for i in range(1000000000):
    if f(i) == 2:
        c += 1
print(c)

print("--- %s seconds ---" % (time.time() - start_time))
