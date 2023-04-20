f = open('file/A!24.txt').readline()
vse = []
for i in range(len(f)-1):
    if f[i] == "A":
        vse.append(f[i+1])
s = list(set(vse))
maxx = 0
li = ''
for i in s:
    if vse.count(i) > maxx:
        maxx = vse.count(i)
        li = i
print(maxx, li)