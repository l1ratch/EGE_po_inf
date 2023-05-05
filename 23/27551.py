def f(x, y):
    if x > y or x == 10:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)


def g(x, y):
    if x > y or x == 9:
        return 0
    if x == y:
        return 1
    return g(x + 1, y) + g(x * 2, y)


print(f(1,  9) * f(9, 20) + g(1,  10) * g(10, 20))