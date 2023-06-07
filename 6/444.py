import turtle as t
t.color('red', 'red')
#t.speed(5)
t.left(90)
k = 30

t.begin_fill()
for i in range(2):
    t.forward(5*k)
    t.right(90)
    t.forward(10*k)
    t.right(90)
t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        s = canvas.find_overlapping(x, y, x, y)
        if s:
            index = s[0]
            color = canvas.itemcget(index, "fill")
            if color == 'red' and len(s) >= 1:
                count += 1
print(count)
t.done()
exit()