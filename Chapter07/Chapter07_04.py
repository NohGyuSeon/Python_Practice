import turtle as t

width = int(input("도형의 가로 길이: "))
height = int(input("도형의 세로 길이: "))

t.shape("turtle")
t.color("blue")
t.pensize(5)
t.goto(width, 0)
t.goto(width, height)
t.goto(0, height) 
t.goto(0, 0)
