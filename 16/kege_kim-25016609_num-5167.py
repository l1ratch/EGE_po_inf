import sys
sys.setrecursionlimit(20000)

def f(n):
    if n >= 10_000:
        return n
    if n < 10_000 and n % 2 == 0:
        return f(n + 2) - 3
    if n < 10_000 and n % 2 != 0:
        return f(n + 2) + 1


print(f(94) - f(80))

F = {10000 : 10000,
     10001 : 10001}

for n in range(9999, 79, -1):
    if n % 2 == 0:
        F[n] = F[n + 2] - 3
    else:
        F[n] = F[n + 2] + 1
print(F[94] - F[80])