a = '11211211211211'
while '11' in a:
    if '112' in a:
        a = a.replace('112', '6', 1)
    else:
        a = a.replace('11', '3', 1)
print(a.count('1')*1 + a.count('2')*2 + a.count('6')*6 + a.count('3')*3)