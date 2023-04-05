f = open('files/47221.txt').readlines()
f = list(map(int, f))
max3 = -20**20
for i in range(len(f)-1):
    if str(f[i])[-1] == "3" and f[i] > max3:
        max3 = f[i]
print(max3)