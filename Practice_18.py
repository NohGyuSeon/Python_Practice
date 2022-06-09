import mycircle as m

print("모듈을 사용하여 원의 넓이와 둘레를 구합니다.")

m.area_cirlce(10)
m.length_cirlce(10)

m.정사각형(100)
m.정삼각형(200)
m.원(150)

var = 100

def func1():
    global var
    var = 10
    print("함수1:", var)
    
def func2():
    var = 1000
    print("함수2:", var)

print("Main :", var)
func1()
print("Main :", var)
func2()
print("Main :", var)
