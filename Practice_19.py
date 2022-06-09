class Person:
    name = None
    age = 0
    def set_info(self, pName, pAge):
        self.name = pName
        self.age = pAge
    def get_info(self):
        print("이름:", self.name, "/ 나이:", self.age)

p1 = Person()
p1.set_info("노규선", 24)

class Circle:
    radius = 0
    def __init__(self, pRadius=10):
        self.radius = pRadius
        print("객체가 생성되었습니다.")        
    def set_radius(self, pRadius):
        self.radius = pRadius
    def cal_area(self):
        area = self.radius * self.radius * 3.14
        print("Area:", area)
    def cal_length(self):
        length = 2 * self.radius * 3.14
        print("Length:", length)

c1 = Circle()      
print(c1.radius)
c1.set_radius(5)
c1.cal_area()
c1.cal_length()
print(c1.radius)
print()

# 성적관리 프로그램
class Student:
    name = None
    kor = None
    end = None
    mat = None
    def __init__(self, name='', kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
    def getSum(self):
        sum = self.kor + self.eng + self.mat
        return sum
    def getAve(self):
        ave = self.getSum() / 3
        return ave

std1 = Student("Kim", 90, 80, 75)
print(std1.getSum())
print(std1.getAve())
print()

import mymodule as md

print(md.pi)
print(md.e)

md.info()

c2 = md.Circle(20)
c2.cal_area()

s1 = md.Square()
s1.cal_area()

print()
