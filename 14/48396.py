for i in '0123456789ABCDEF':
    num1 = int('2' + i + '84', 19)
    num2 = int('2B3' + i, 16)
    if ((num1 + num2) % 88) == 0:
        print(((num1 + num2) // 88))