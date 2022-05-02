import math as m

print(m.sin(0))
print(m.cos(0))
print(m.sqrt(5))
print(m.log(10))
print()

print(m.pi)
print(m.e)
print(m.tau)
print(m.inf)
print()

r = float(input("r:"))
length = 2 * m.pi * r
area = m.pow(m.pi, 2) * r
print("%.2f, %.2f" % (length, area))
print()

abs = m.fabs(-5.7)
fact = m.factorial(5)
print(abs)
print(fact)
print()

print(m.gcd(120, 860))
print(m.radians(30))
print(m.degrees(m.pi))
print(m.log(m.e))
print(m.log10(1000))
