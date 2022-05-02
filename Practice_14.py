t1 = " Hello Python "
small = t1.lower()
large = t1.upper()
cap = t1.capitalize()
t2 = t1.lstrip()
t3 = t1.rstrip()
t4 = t1.strip()
print(small)
print(large)
print(cap)
print(t2, len(t2))
print(t3, len(t3))
print(t4, len(t4))
print()

text = "hello useful python"
text = text.replace("useful" , "powerful")
print(text)
print()

# 주민등록번호 : 2000년 이전 출생
num = input("주민번호 앞자리 입력: ")

y = "19" + num[0:2]
m = num[2:4]
d = num[4:6]
x = num[7:8]

age = 2022 - int(y) + 1
print("당신은 %s년에 태어났군요." % y)
print("당신의 생일은 %s월 %s일 이군요." % (m, d))
print("당신은 올해 %d살이군요." % age)
if int(x) == 1 or int(x) == 3:
    print("당신은 남성이군요")
else:
    print("당신은 여성이군요")

bool = "hello" in text
print(bool)

while True:
    query = input("\n질문 입력>> ")
    if query.find("안녕") >= 0:
        print("안녕하세요.")
    elif query.find("파이썬") >= 0:
        print("파이썬 존나 마스터 하세요.")
    elif query.find("날씨") >= 0:
        print("날씨가 존나게 더워요.")
    elif query.find("그만") >= 0:
        break
    else:
        print("뭔 소리? 코딩해서 알려주세요")

test = "AABCD"
for x in range(0, 5, 1):
    print("[%d] --> [%s]" % (x, test[x]))
print(test.count("A"))
