pi = 3.14
e = 2.71

def info():
    print("이 모듈은 여러 클래스와 변수를 포함하고 있습니다")

class Circle:
    radius = 0
    def __init__(self, pRadius=10):
        self.radius = pRadius
    def set_radius(self, pRadius):
        self.radius = pRadius
    def cal_area(self):
        area = self.radius * self.radius * 3.14
        print("Area:", area)
    def cal_length(self):
        length = 2 * self.radius * 3.14
        print("Length:", length)

class Square:
    size = 0
    def __init__(self, pSize=10):
        self.size = pSize
    def set_radius(self, pSize):
        self.size = pSize
    def cal_area(self):
        area = self.size * self.size
        print("Area:", area)
    def cal_length(self):
        length = 4 * self.size
        print("Length:", length)
        