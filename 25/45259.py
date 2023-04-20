for i in range(123450708, 10**9):
    if i % 23 == 0:
        num = str(i)
        if num[:5] == '12345' and num[-1] == '8' and num[-3] == '7':
            print(i, i//23)