num = input("입력: ")

y = int(num[0:4])
m = int(num[4:6])
d = int(num[6:8])

age = 2022 - y + 1
print("출생연도: %d년" % y)
print("생일: %d월 %d일" % (m, d))
print("나이: %d살" % age)
