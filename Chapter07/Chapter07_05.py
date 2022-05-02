import turtle as t
import math

r = int(input("반지름을 입력하세요: " ))
circle = pow(r, 2) * math.pi
print("원의 넓이는 %d입니다" % circle)

t.shape("turtle")
t.circle(200)
