from tkinter import E


number = int(input("input: "))

if number <= 0:
    print("Wrong Input") 
elif number % 3 == 0:
    print("3의 배수입니다.")
else:
    print("3의 배수가 아닙니다.")
    