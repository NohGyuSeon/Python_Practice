quiz = int(input("quiz score: "))
middle = int(input("middle score: "))
final = int(input("fimal score: "))

result = quiz*0.2 + middle*0.3 + final*0.5

if result >= 70:
    print("PASS")
else:
    print("FAIL")
    