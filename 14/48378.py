for i in '0123456789ABCDEFGHI':
    num1 = int('321' + i + '4', 19)
    num2 = int('498' + i + '9', 19)
    if ((num1 + num2) % 23) == 0:
        print(((num1 + num2) // 23))