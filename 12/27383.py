a = '121212121211111'
while '12' in a:
    a = a.replace('12', '4', 1)
print(a.count('1') + a.count('2')*2 + a.count('4')*4)

# 25 чисел получаем при 5 двойках в строке