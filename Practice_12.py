# 표준 몸무게 계산하기
for h in range(150, 181, 3):
    weight = (h - 100) * 0.9
    print("Height: %d cm -> Weight: %.1f kg" % (h, weight))
    print()
    
# 팩토리얼 값 구하기
num = int(input("Factorial : "))
fac = 1
for i in range(1, num+1):
    fac *= i
print("Result:", fac)
print()

# 369 게임하기
for i in range(1, 100):
    if (i - int(i / 10) * 10) % 3 == 0 and (i - int(i / 10) * 10) != 0:
        print("박수")
    else:
        print(i)
print()

# 구구단 퀴즈
import random as r
sum = 0
for i in range(5):
    a = r.randint(1, 9)
    b = r.randint(1, 9)
    solution = a * b

    num = int(input("%d x %d = " % (a, b)))
    if solution == num:
        print("정답입니다.")
        sum += 20
    else:
        print("오답입니다.")

print("최종점수", sum)
print()

# 소수 판별하기
num = int(input("어떤 수를 판별할까요? "))
prime = True
i = 2
while i < num:
    if num % i == 0:
        prime = False
        break
    i += 1

if prime == True:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
print()

n = int(input("어떤 수를 판별해줄까요? "))
success = True
for t in range (2, n, 1):
    if n % t == 0:
        success = False
        break

if success == True:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
print()

# 최대 공약수 구하기
n1 = int(input("작은 수 입력:"))
n2 = int(input("큰 수 입력:"))

# gcd = 1
# t = 2
# while t <= n1:
#     if (n1 % t == 0) and (n2 % 2 == 0):
#         gcd = t
#     t += 1
# print("%d와 %d의 최대 공약수는 %d입니다." % (n1, n2, gcd))

while True:
    if n1 == n2:
        print("최대공약수:", n1)
        break
    else:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1

# 피보나치 수열 구하기
f = [1, 1]
# 1, 1, 2, 3, 5, 8, 13, ...
i = 2
num = int(input("몇 번째 값을 출력시킬까요?"))

while i < num:
    f.append(f[i-2] + f[i-1])
    i += 1
print("Result :", f[i-1])

# 피보나치 수열 구하기
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("몇 번째 값을 출력시킬까요?"))
f = fibo(num)
print("Result:", f)
