while True:
    a = input()
    if a == "exit":
        break
    if (int(a) % 4 == 0 and int(a) % 100 != 0) or (int(a) % 400 == 0):
        print(a, "is a leap year.")
    else:
        print(a, "is not a leap year.")
        