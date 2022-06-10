class PythonLecture:
    score1 = None
    score2 = None
    score3 = None
    absent = None
    def __init__(self, score1=0, score2=0, score3=0, absent=0):
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.absent = absent
    def getSum(self):
        sum = self.score1 + self.score2 + self.score3
        return sum
    def getAve(self):
        ave = self.getSum() / 3
        return ave
    def getWeightAve(self):
        ave = self.score1 * 0.2 + self.score2 * 0.3 + self.score3 * 0.5
        return ave
    def getScore(self):
        if self.absent < 4:
            if self.getWeightAve() >= 90:
                return 'A'
            elif self.getWeightAve() >= 80:
                return 'B'
            elif self.getWeightAve() >= 70: 
                return 'C'
            elif self.getWeightAve() >= 60: 
                return 'D'
            else:
                return 'F'
        else:
            return 'F'
        
def View():
    array = [0, 0, 0]
    std_result = [0, 0, 0]
    print("파이썬 수업 성적 산출")
    for i in range(3):
        print(i+1, end="")
        array[i] = list(map(int, input("번 학생 > ").split(',')))
        
    for i in range(3):
        std_result[i] = PythonLecture(array[i][0], array[i][1], array[i][2], array[i][3])
        
    print()
    print("=== 분석결과 ===\n번호 산출점수 학점")
    for i in range(3):
        print(i+1, end="")
        print("번", std_result[i].getWeightAve(), std_result[i].getScore(), sep='\t')
        
View()
