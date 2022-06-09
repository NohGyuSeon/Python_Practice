import math as m

a, b = map(int, input().split())

a_r = m.radians(a)
b_r = m.radians(b)

sin = m.sin(a_r)
cos = m.cos(b_r)

if sin > cos:
    sub = sin-cos
else:
    sub = cos-sin

print("%.2f" % sub, end=" ")
print("%.2f" % (sin*cos))

# import math as m
# data = input().split()

# s = m.sin(m.radians(float(data[0])))
# c = m.cos(m.radians(float(data[1])))

# print("%.2f %.2f" % (abs(s-c), s*c))
