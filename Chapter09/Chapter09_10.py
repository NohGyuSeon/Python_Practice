height = int(input("input height: "))
weight = int(input("input weight: "))
range = (weight / ((height - 100) * 0.9)) * 100

if range < 85:
    print("저체중 많이 쳐먹고 운동해라")
elif range < 115:
    print("정상")
elif range < 130:
    print("운동 빡세게 해라")
else:
    print("엥간 쳐먹고 운동해라")
