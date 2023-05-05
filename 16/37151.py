f = {0: 0,
     1: 0
     }

for n in range(2, 50):
    if n % 2 != 0:
        f[n] = f[n - 1] + 3 * n ** 2
    else:
        f[n] = n//2 + f[n - 1] + 2
print(f[49])
