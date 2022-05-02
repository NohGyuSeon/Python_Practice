def func(x):
    result = x**2 + 5*x + 3
    return result

# 여기서부터 실행됨
x = 10
y = func(x)
print("f(%d) = %d" % (x, y))

def print_age(year):
    age = 2022 - year + 1
    print("%d년생의 나이는 %d살 입니다." % (year, age))

print_age(200)
print_age(2002)
print_age(2020)

def greeting(name, n):
    for i in range(n):
        print("안녕! ", name)

greeting("NGS", 5)
greeting("MIKKY", 3)

# 교재 202쪽 5번, 7번, 8번
