from turtle import *

color('black', 'green')
left(90)
k = 30

begin_fill()
for i in range(6):
    right(36)
    forward(10*k)
    right(36)
end_fill()

c = 0
canv = getcanvas()
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        s = canv.find_overlapping(x, y, x, y)
        if s:
            ind = s[0]
            color = canv.itemcget(ind, 'fill')
            if color == 'green' and len(s) == 1:
                c += 1
print(c)
done()