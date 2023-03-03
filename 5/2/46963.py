for i in range(1, 100):
    s = bin(i)[2:]
    count1, count0 = 0, 0
    for j in range(0, len(s)):
        if j % 2 != 0 and s[j] == "1":
            count1 += 1
        elif s[j] == "0":
            count0 += 1