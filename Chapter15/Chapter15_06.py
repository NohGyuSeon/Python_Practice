list = []
sum = 0

for i in range(0, 5, 1):
    n = int(input("input : "))
    list.append(n)
    sum += n
    
for i in range(0, 5, 1):
    print(i+1, "번 학생 점수", list[i])

avg = sum / len(list)

print("성적 합계: %d / 성적 평균: %.2f" % (sum, avg))
