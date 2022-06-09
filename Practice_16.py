dict = { "강아지":"dog", "고양이":"cat", "노규선":"human"}
print(dict.keys())
print(dict.values())
print()

print(dict["노규선"])
print()

lang = {"C":1972, "C++":1980, "JAVA":1995, "Python":1991}

test = input("검색하고자 하는 언어는? ")
if test in lang:
    print(lang[test])
else:
    print("알 수 없는 정보입니다.")
print()

del lang["C++"]
print(lang)
print()

lang.clear()
print(lang)
print()

lang = {"C":1972, "C++":1980, "JAVA":1995, "Python":1991}
KeyList = lang.keys()

for x in KeyList:
    print(x)
print()

for item in lang.items():
    print(item)
    print("%s -> %d" % (item[0], item[1]))
print()

item = {}

for i in range(3):
    code = input("상품의 코드를 입력하세요:")
    price = int(input("상품의 가격을 입력하세요:"))
    if code in item:
        print("해당 코드는 이미 입력되어 있습니다.")
    else:
        item[code] = price

for i in item.keys():
    print("%s코드에 해당되는 상품의 가격은 %d 입니다." % (i, item[i]))
sum = 0

for i in item.values():
    sum += i
print("입력된 상품들의 총 합은 %d원 입니다." % sum)
print()
