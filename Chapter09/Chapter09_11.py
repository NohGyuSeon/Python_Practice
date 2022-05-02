height = int(input("input height: "))
weight = int(input("input weight: "))
height = height / 100
BMI = (weight / (height * height)) 
  
if BMI < 20:
    print("저체중 많이 쳐먹고 운동해라")
elif BMI < 25:
    print("정상")
elif BMI < 30:
    print("운동 빡세게 해라")
elif BMI < 40:
    print("적당히 쳐먹고 운동 빡세게 해라")
else:
    print("엥간 쳐먹고 운동부터 쳐해라")
    