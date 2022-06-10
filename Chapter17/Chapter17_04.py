fp = open(r"C:\\NGS\\subject.txt", "r", encoding='UTF8')
data = []
sum = [0, 0, 0]
avg = [0, 0, 0]

for line in fp.readlines()[1:11]:
    data.append(line.strip().split(","))
    
for i in range(10):
    print(data[i])

for i in range(10):
    for j in range(0, 3, 1):
        sum[j] += int(data[i][j])
        
for i in range(3):
    avg[i] = sum[i] / len(data)
    
print("과목의 평균 점수 → 국어: %.2f, 영어: %.2f, 수학: %.2f" % (avg[0], avg[1], avg[2]))

fp.close()
