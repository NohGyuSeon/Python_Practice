iq = 130
age = 24
if (age >= 20 and iq >= 130):
    print("True")
else:
    print("False")

score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print("장학금 대상입니다.")
print("수고하셨습니다.")

t = int(input("시간을 입력하세요 : "))
if t < 6:
    cal_t = 24 + (t - 6)
else:
    cal_t = t - 6
print("이전 시간은 ", cal_t, "입니다.")

# 짝수/홀수 판별 프로그램

num = int(input("양의 정수 n 입력 : "))

if num < 0: # 음수
    print("판별할 수 없는 수를 입력하셨습니다.")
else: # 양수
    print("정수 %d를 입력하셨군요," % num)
    if num % 2 == 0: # 짝수
        print("짝수")
    else: # 홀수
        print("홀수")

score2 = int(input("시험 점수를 입력하세요: "))
if score2 >= 90:
    print("시험을 아주 잘 봤군요. 축하합니다.")
elif score2 >= 80:
    print("시험을 괜찮게 봤군요. 수고하셨습니다.")
elif score2 >= 90:
    print("시험을 좀 못 봤군요. 다음에는 잘 보도록 해요.")
else:
    print("완전히 조지셨네요!")
    