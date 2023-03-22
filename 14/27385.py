a = 343**5 + 343**4 + 49**6 - 7**13 - 21
n = a
s = ''
m = set()
while n != 0:
    s += str(n % 7)
    n //= 7
    m.add(n % 7)
print(len(m))


