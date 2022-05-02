n = int(input("input n: "))
m = 1

print("구구단 %d단" % n)

while True:
    if n < 2 or n > 9:
        print("Wrong input")
        break
    else:
        while m <= 9:
            print("%d x %d = %d" % (n, m, n*m))    
            m += 1
        break
    