A = int(input("input A: "))
B = int(input("input B: "))

sum = 0

if A <= B:
    for i in range(A, B+1, 1):
        sum += i
    print(sum)
