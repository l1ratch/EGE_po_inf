import turtle as t

t.color('red', 'red')
t.left(90)
k = 30
t.speed(10)

t.begin_fill()
for i in range(10):
    t.forward(9*k)
    t.right(90)
    t.forward(2*k)
    t.right(90)
t.end_fill()

c = 0
canv = t.getcanvas()
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        s = canv.find_overlapping(x,y,x,y)
        if s:
            ind = s[0]
            color = canv.itemcget(ind, 'fill')
            if color == 'red' and len(s) >= 1:
                c += 1
print(c)
t.done()


