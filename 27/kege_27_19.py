f = open('files/27_A_7627.txt')
k = int(f.readline())
n = int(f.readline())
A = []
for i in range(0, n):
    num = int(f.readline())
    A.append(num)
for i in range(0, n, k):
