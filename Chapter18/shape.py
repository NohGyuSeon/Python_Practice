import turtle as t

def rectangle(w, h):
    t.fillcolor("blue")
    t.begin_fill()
    t.goto(w, 0)
    t.goto(w, h)
    t.goto(0, h)
    t.goto(0, 0)
    t.end_fill()
    return 0

def cycle(r):
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    return 0

def equal_rectangle(x, y, size):
    t.goto(x, y)
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    for i in range(4):
        t.left(90)
        t.forward(size)
    return 0

def equal_cycle(x, y, r):
    t.goto(x, y)
    t.forward(r)
    t.left(90)
    t.circle(r)
    return 0
    