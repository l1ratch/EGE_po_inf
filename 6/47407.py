from turtle import *

left(90)
k = 30

color('black', 'green')
begin_fill()
for i in range(4):
    forward(8*k)
    right(90)
end_fill()

color('blue', 'red')
begin_fill()
for i in range(3):
    forward(12*k)
    right(120)
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