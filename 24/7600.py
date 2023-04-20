f = open('file/24_7600.txt').readline()
f = f.replace("Q", "!").replace("R", "!").replace("S", "!")
c = 1
m = 0
for i in range(len(f)-1):
    if f[i] == "!" and f[i+1] == "!":
        m = max(m, c)
        c = 1
    else:
        c += 1
print(m)

f2 = open('file/24_7600.txt').readline()
f2 = f2.replace("Q", "!").replace("R", "!").replace("S", "!").replace("!!", "! !").split()
m2 = 0
for i in f2:
    m2 = max(len(i), m2)
print(m2)
