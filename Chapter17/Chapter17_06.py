fp = open(r"C:\\NGS\\calculator.txt", "w")

try:
    x, y = map(int, input().split(" "))
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    fp.write("사칙연산 결과\n%d\n%d\n%d\n%.2f" % (add, sub, mul, div))
except ZeroDivisionError:
    fp.write("입력한 정수가 0이 아닌 숫자로 입력해야 합니다.")
    
fp.close()
