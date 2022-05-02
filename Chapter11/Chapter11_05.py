# 팩토리얼
num = int(input("Factoiral: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i

print("Factorial reulst: %d" % fact)
print()

# 369
n = 1
while n <= 100:
    if n % 3 == 0 or n % 10 == 3:
        print("박수")
    else:
        print(n)
    n = n + 1

# 구구단 퀴즈
import random as r

sum = 0
for i in range(5):
    a = r.randint(1, 9)
    b = r.randint(1, 9)
    answer = a * b

    num = int(input("%d x %d = " % (a, b)))
    if answer == num:
        print("정답입니다")
        sum += 20
    else:
        print("오답입니다")

print("최종점수", sum)
print()

# 소수 판별하기
value = int(input("어떤 숫자를 판별할까요? "))
prime = True
i = 2
while i < value:
    if value % i == 0:
        prime = False
        break
    else:
        i += 1

if prime == True:
    print("소수입니다")
else:
    print("소수가 아닙니다")
print()

# 피보나치 수열의 최댓값과 index 값

data = input().split()
n = int(data[0])
k = int(data[1])

def fibo(n, k):
    count = k
    bool = False
    f = [1, 1]    
    i = 2
    while True:
        f.append(f[i-1] + f[i-2])
        if f[i-1] > n:
            if i-1 > k:
                break
            else:
                i += 1
                count -= 1
                bool = True
        else:
            i += 1

    if bool:
        return f[count], f[k-1]
    else:
        return f[i-2], f[i-1]

x, y = fibo(n, k)    

print(x, y)
print()

# 사칙연산
cal = input().split()

if cal[1] == '+':
    print("% .5f" % (float(cal[0]) + float(cal[2])))
elif cal[1] == '-':
    print("% .5f" % (float(cal[0]) - float(cal[2])))
elif cal[1] == '*':
    print("% .5f" % (float(cal[0]) * float(cal[2])))
elif cal[1] == '/':
    if cal[2] == '0':
        print("NaN")
    else:
        print("% .5f" % (float(cal[0]) / float(cal[2])))
elif cal[1] == '%':
    print("%.5f" % (float(cal[0]) % float(cal[2])))
print()

# 유클리디안 최대공약수 최소공배수
array = input().split()

n1 = int(array[0])
n2 = int(array[1])

def GCD(n1, n2):
    while True:
        if n1 <= 0 or n2 <= 0:
            break
        if n1 == n2:
            gcd = n1
            break
        else:
            if n1 > n2:
                n1 = n1 - n2
            else:
                n2 = n2 - n1
    return gcd

n1 = int(array[0])
n2 = int(array[1])

def LCM(x, y):
    result = (n1*n2) // GCD(n1, n2)
    return result

if n1 <= 0 or n2 <= 0:
    print("wrong input")
else:
    print("GCD: %d / LCM: %d" % (GCD(n1, n2), LCM(n1, n2)))
print()
