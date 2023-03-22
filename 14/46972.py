a = 5 * (343 ** 8) + 4 * (49 ** 12) + 7 ** 14 - 98
n = a
s = ''
while n != 0:
    s += str(n % 7)
    n //= 7
s = s[::-1]
print(s.count('0'))
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))
print(s.count('4'))
print(s.count('5'))
print(s.count('6'))