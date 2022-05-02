import turtle as t

def line(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

    return

t.color("red")
line(-500, 0, 500, 0)
t.color("black")
t.write("y=x")
line(0, -500, 0, 500)

t.goto(0, 0)
t.write("(0, 0)")
