fp = open(r"C:\\Users\\NOH GYUSEON\\OneDrive\\바탕 화면\\조선대\\3학년 1학기\\계산적사고와문제해결\\test.txt", "w")
for t in range(2, 10, 1):
    fp.write("\n구구단 %d 출력" % t)
    for k in range(1, 10, 1):
        fp.write("%d x %d = %d" % (t, k, t*k))

fp.close()

# while True:
#     line = fp.readline()
#     if len(line) == 0:
#         break
#     print(line, end="")

# fp.close()

try:
    text = input("출생년도 입력: ")
    year = int(text)
    age = 2022 - year + 1
    print("당신은 %d살 입니다." % age)
except:
    print("예상치 못한 상황으로 종료합니다.")

print("감사합니다.")


try:
    t = input("정수 입력: ")
    n = int(t)
    m = 100 / n
    print("100을 %d로 나눈 몫: %d" % (n, m))
    print("입력한 두번째 숫자: %c" % t[1])
except ValueError:
    print("입력한 값이 정수가 아닙니다.")
except ZeroDivisionError:
    print("입력한 정수가 0이 아닌 숫자로 입력해야 합니다.") 
except IndexError:
    print("인덱스 범위가 잘못되었습니다.")

try:
    name = input("파일명을 입력하세요: ")
    fp = open(name, "r")
    for line in fp.readline():
        print(line, end="")
    fp.close()
except:
    print("해당 파일이 존재하지 않습니다.")
    