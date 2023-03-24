for i in '0123456789':
    num1 = int('4C' + i + '4', 15)
    num2 = int(i + '62A', 13)
    if ((num1 + num2) % 121) == 0:
        print(((num1 + num2) // 121))