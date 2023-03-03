s = ''
x = 4**12 + 2**32 - 16
while x != 0:
    s = s + str(x % 2)
    x = x // 2
s = s[::-1]
print(s.count("1"))