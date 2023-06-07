import turtle as t

t.color('black', 'red')
t.left(90)
k = 4
t.speed(10)

t.begin_fill()
for i in range(2):
    t.forward(10 * k)
    t.right(60)
    t.forward(10 * k)
    t.right(120)
t.end_fill()

c = 0
canvas = t.getcanvas()
for x in range(-100 * k, 100 * k, k):
    for y in range(-100 * k, 100 * k, k):
        s = canvas.find_overlapping(x, y, x, y)
        if s:
            ind = s[0]
            color = canvas.itemcget(ind, "fill")
            if color == 'red' and len(s) == 1:
                c += 1
print(c)
t.done()
