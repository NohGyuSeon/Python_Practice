height = float(input())
weight = float(input())

height_m = height / 100

BMI = weight / (height_m * height_m)

print("BMI: {:.2f}".format(BMI))

if BMI < 18.5:
    print("Slim")
elif BMI >= 18.5 and BMI < 25.0:
    print("Standard")
elif BMI >= 25.0 and BMI < 30.0:
    print("Obesity")
else:
    print("Extremely Obesity")
    