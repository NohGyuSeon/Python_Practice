year = int(input("input year: "))
age = 2022 - year + 1

if age <= 7:
    print("어린이")
elif age <= 13:
    print("초딩")
elif age <= 16:
    print("중딩")
elif age <= 19:
    print("고딩")
elif age <= 26:
    print("대딩")
else:
    print("직딩")
    