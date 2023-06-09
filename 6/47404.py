from turtle import *

left(90)
k = 30

color('black', 'green')
begin_fill()
for i in range(4):
    forward(10*k)
    right(90)
right(30)
end_fill()

color('blue', 'red')
begin_fill()
for i in range(2):
    forward(6*k)
    right(60)
    forward(6*k)
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