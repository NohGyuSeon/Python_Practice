# 학교 종 멜로디 구현하기
"""
import winsound
import time

음계 = {'도':523, '레':587, '미':687, '파':698,
        '솔':783, '라':880, '시':987, '또':1046 }
학교종 = "솔솔라라솔솔미 솔솔미미레 솔솔라라솔솔미 솔미레미도"

for i in 학교종 :
    if i == ' ':
        time.sleep(1)
    else :
        winsound.Beep(음계[i], 300)
"""

text = """Hello World!
My name is NGS"""
print(text)
print()
print("Hello World\nHello World")
print("Hello World\tHello World")
print("Hello \\World")
print("Hello \'World\'")
print("Hello \"World\"")

x = 5
y = 3
print("x + y =", x + y)
print(x, "+", y, "=", x + y)

print("Hello", end=" ")
print("Easy", end=" ")
print("Powerful Python", end='***')

print()

print("Hello", "Easy", "Python", sep=" ")
print("Hello", "Easy", "Python", sep="")
print("Hello", "Easy", "Python", sep="\t")
print("Hello", "Easy", "Python", sep=",")
print("Hello", "Easy", "Python", sep="\n")

x = "2019"
y = "2000"

print(int(x) - int(y))
print()

a = 1
b = 10
print('a - ', bin(a))
print('b - ', bin(b))

n1 = 10
n2 = 100
n3 = 123123123123123123123123

import sys
print(sys.getsizeof(n1))
print(sys.getsizeof(n2))
print(sys.getsizeof(n3))
print()

n1 = 123123123123123123123123
print(sys.getsizeof(n1))
print()

f1 = 1.2
f2 = 1.23412341234
f3 = 1.234234234234234234234234234

print(sys.getsizeof(f1))
print(sys.getsizeof(f2))
print(sys.getsizeof(f3))

for i in range(65, 96, 1):
    print(i, "-->", chr(i))

print()

for i in range(65, 96, 1):
    print(chr(i), "-->", i)

print()

text = "HELLO"

for i in text:
    print(i, "->", ord(i), ":", bin(ord(i)))

letter = "Dude! Keep it up!!!"
encodeLetter = ""

for ch in letter:
    num = ord(ch)
    encodeLetter += chr(num-1)

print("원문: ", letter)
print("암호: ", encodeLetter)

decodeLetter = ""

for ch in encodeLetter:
    num = ord(ch)
    decodeLetter += chr(num+1)

print("암호 해제: ", decodeLetter)
