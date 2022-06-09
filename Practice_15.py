a = list(range(1, 1001, 4))
print(a)
print()

print(len(a))
print(sum(a))
print(max(a))
print(min(a))
print()

a = [10, 20, 30]
print(a[0])
print(a[1])
print(a[2])
print(a)
print()

a.append(40)
a.append(50)
print(a)
print()

b = [4, 5, 6]
a.extend(b)
c = [7, 8, 9]
a += c
a.insert(11, 100)
print(a)
a.remove(100)
print(a)
print()

scores = []
for i in range(5):
    value = int(input("성적입력: "))
    scores.append(value)

print(scores)
print("Totoal:", sum(scores))
print("Average:", sum(scores)/len(scores))
print()

# 키와 표준 몸무게
hlist = list(range(150, 181, 3))
wlist = [ (h-100)*0.9 for h in hlist ]

for i in range(len(hlist)):
    print("{0:2d} {1:5d}cm {2:6.1f}kg".format(i+1, hlist[i], wlist[i]))
print()

# 튜플 -> 값을 변경할 수 없음 => 리스트로 변경하여 사용
tu_test = (10, 20, 30, 40)
print(tu_test[0])
print(tu_test[1])
print(tu_test[2])
print(tu_test[3])
print(tu_test)
print()

test = list(tu_test)
test.append(50)
print(test)
print()
