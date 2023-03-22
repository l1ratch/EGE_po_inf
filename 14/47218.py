for i in '0123456789ABCDE':
    num1 = int('123' + i + '5', 15)
    num2 = int('1' + i + '233', 15)
    if ((num1 + num2)%14) == 0:
        print(((num1 + num2) // 14))
