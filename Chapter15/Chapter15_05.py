list = []
avg = 0

for i in range(0, 4, 1):
    n = int(input("input : "))
    list.append(n)

for i in range(0, 4, 1):
    avg += list[i]*0.1*(i+1)


for i in range(0, 4, 1):
    print(i+1, "차 점수", list[i])

print("평균 점수", avg)
