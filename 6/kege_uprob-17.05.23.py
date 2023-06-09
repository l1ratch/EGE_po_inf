from turtle import *

color('black', 'red')
left(90)
k = 15
speed(10)

begin_fill()
right(315)
for i in range(2):
    forward(12*k)
    right(45)
    forward(6*k)
    right(135)
end_fill()

c = 0
canv = getcanvas()
for x in range(-100*k, 100*k, k):
    for y in range(-100 * k, 100 * k, k):
        s = canv.find_overlapping(x,y,x,y)
        if s:
            ind = s[0]
            color = canv.itemcget(ind, 'fill')
            if color == 'red' and len(s) == 1:
                c += 1
print(c)
done()


