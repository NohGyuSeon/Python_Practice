n = 1

while n <= 5:
    print("파이썬 재밌네")
    n = n + 1
print("파이썬 쉽네")
print()

import time
m = 10
while m <= 100:
    print(m)
    m += 10
    # time.sleep(1)
print()
print("종료합니다.")

n = 1
while n <= 9:
    m = 1
    print("구구단 %d단" % n)
    while m <= 9:
        print("%d x %d = %d" % (n, m, m*n))
        m += 1
    n += 1
print()

import random as r
# 10-100 10단위
print(r.randint(1, 10) * 10)
print(r.randrange(10, 100, 10))
print(int(int(r.random() * 90) / 10) * 10 + 10)
print()

print("주사위 던지기")
val = 0
while val != 6:
    val = r.randint(1, 6)
    print("주사위의 값 : %d" % val)
    time.sleep(1)
print()

for t in range (1, 11, 1):
    print("Count %d" % t)
print("종료합니다.")
print()

n = 1
while n <= 10:
    print("Count %d" % n)
    n += 1
print("종료합니다.")
print()

for t in range (1, 11): # 1씩 증가
    print("Count %d" % t)
print("종료합니다.")
print()

for t in range (11): # 0부터 1씩 증가
    print("Count %d" % t)
print("종료합니다.")
print()

for h in range(150, 163, 3):
    weight = (h - 100) * 0.9
    print("키: %dcm, 제안: %.1fkg" % (h, weight))

n = int(input("몇까지 셀까요? "))
for i in range(1, n+1, 1):
    print("Count", i)
print("End")
print()

n = int(input("몇부터 셀까요? "))
m = int(input("몇까지 셀까요? "))
for i in range(n, m+1):
    print("Count", i)
print("End")
print()

n = int(input("몇부터 셀까요? "))
m = int(input("몇까지 셀까요? "))
i = n
while i <= m:
    print("Count", i)
    i += 1
print("End")
print()

n = 1
s = 0
while n <= 500:
    s += n
    n += 3
print(s)
print()

s = 0
for n in range(1, 501, 3):
    s += n
print(s)
print()

start = int(input("input start: "))
end = int(input("input end: "))
sum = 0

if start > end:
    print("X")
else:
    for n in range(start, end+1, 1):
        sum += n
    print(sum)
    