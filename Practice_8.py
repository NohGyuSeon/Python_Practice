name = input("이름이 뭐에요? ")
year = int(input("몇 년도에 태어났어요? "))

print("안녕하세요 %s씨 반가워요." % name)
print("당신은 %d년도에 태어났군요." % year)
print("당신은 올해 %d살 이군요." % (2022-year+1))

x = 15
y = x * x * 3.14
text = '반지름 = {0}, 원넓이 = {1}'.format(x, y)
print(text)

x = 15
y = x * x * 3.14
text = '반지름 = {0:d}, 원넓이 = {1:f}'.format(x, y)
print(text)

price = 3000000
text = '제품가격은 {0:,d}입니다.'.format(price)
print(text)

a = 1
b = 4
c = 5
d = 10

print("a : {0:08b}".format(a))
print("a : {0:08b}".format(b))
print("a : {0:08b}".format(c))
print("a : {0:08b}".format(d))

for i in range(65, 91, 1):
    print("{0:d} -- {0:c} -- {0:08b}".format(i))
    