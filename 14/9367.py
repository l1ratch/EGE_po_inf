a = 125 + 25**3 + 5**9
n = a
s = ''
while n != 0:
    s += str(n % 5)
    n //= 5
s = s[::-1]
print(a)
print(s.count('0'))

# код из задачи 13362