import turtle as t

def area_cirlce(r):
    result = r * r * 3.14
    print("Area :", result)

def length_cirlce(r):
    result = 2 * r * 3.14
    print("Length :", result)

def 정사각형(size):
    for i in range(4):
        t.forward(size)
        t.left(90)
    return 0

def 정삼각형(size):
    for i in range(3):
        t.forward(size)
        t.left(120)
    return 0

def 원(size):
    t.circle(size)    
    return 0
    