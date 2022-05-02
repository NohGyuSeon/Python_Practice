import turtle as t

num = int(input("몇각형을 그려줄까요? "))

t.shape("turtle")
t.shapesize(3)

for i in range(num):
    t.forward(50)
    t.right(360/num)
    