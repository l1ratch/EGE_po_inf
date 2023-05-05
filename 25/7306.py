def prost(n):
    c_ = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            c_ += 1
    if c_ == 0:
        return True
    else:
        return False

c = 0
for i in range(2, 10**5):
    if prost(i):
        c += 1
        if prost(c) and i != 2:
            if i > 1707:
                num = str(i)
                if num[0] == '1' and num[-1] == '7' and num[-3] == '7':
                    print(i, c)