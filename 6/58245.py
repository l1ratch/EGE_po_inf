from turtle import *

left(90)
k = 10

color('black', 'green')
begin_fill()
right(60)
for i in range(2):
    forward(10*k)
    right(120)
    forward(5*k)
    right(240)
right(120)
forward(3*k)
right(90)
forward(20*3**0.5*k)
right(90)
forward(8*k)
right(120)
for j in range(1):
    forward(10*k)
    left(120)
    forward(5*k)
    left(240)
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