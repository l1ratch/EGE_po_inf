c = 0
for a in range(3, 50):
    s = '>' + '1' * a + '2' * a + '3' * a
    while ('>1' in s) or ('>2' in s) or ('>3' in s):
        if '>1' in s:
            s = s.replace('>1', '22>3')
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>3' in s:
            s = s.replace('>3', '11>2')
    if (s.count('1')*1 + s.count('2')*2 + s.count('3')*3)%7==0:
        c += 1
print(c)