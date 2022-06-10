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
        
std = PythonLecture(90, 80, 70, 3)

print(std.getSum())
print(std.getAve())
print(std.getWeightAve())
print(std.getScore())
