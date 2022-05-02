print("=== 원리금 계산 프로그램 ===")

seed_money = int(input("저축 금액 입력 -> "))
rate = seed_money * 0.0375
tax = rate * 0.15
result = seed_money + rate - tax

print("원금: {:,}원".format(seed_money, ','))
print("이자: {:,}원".format(int(rate), ','))
print("세금: {:,}원".format(int(tax), ','))
print("최종: {:,}원".format(int(result), ','))
