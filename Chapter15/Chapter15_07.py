import random as r

kor = []
eng = []
mat = []
sum_kor = 0
sum_eng = 0
sum_mat = 0

for i in range(11):
    kor.append(r.randint(0, 100))
    eng.append(r.randint(0, 100))
    mat.append(r.randint(0, 100))
    sum_kor += kor[i-1]
    sum_eng += eng[i-1]
    sum_mat += mat[i-1]
    
for i in range(0, 10, 1):
    print(i+1, "번째 학생의 점수: %d %d %d" % (kor[i], eng[i], mat[i]))
print()

avg_kor = sum_kor / 10
avg_eng = sum_eng / 10
avg_mat = sum_mat / 10
    
print("과목별 성적 평균 → 국어: %.2f 영어: %.2f 수학: %.2f" % (avg_kor, avg_eng, avg_mat))
