for x in range(0, 17):
    s = int(10+x+0) + int(150+x+1515)
    if s % 13 == 0:
        s = s//13
        #n = int(s, 17)
print(s)