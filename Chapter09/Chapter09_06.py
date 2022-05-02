number = int(input("input: "))

if number <= 0:
    print("Wrong Input")
else:
    print("%d은" % number)
    if number % 2 == 0:
        print("2의 배수입니다.")
    else:
        print("2의 배수가 아닙니다.")
    if number % 3 == 0:
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")
    if number % 5 == 0:
        print("5의 배수입니다.")
    else:
        print("5의 배수가 아닙니다")
        