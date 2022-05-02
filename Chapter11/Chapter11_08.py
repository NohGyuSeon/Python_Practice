n = 1
while n <= 5:
    m = 1
    print("구구단 %d단" % n)
    while m <= 9:
        print("%d x %d = %d" % (n, m, m*n))
        m += 1
    n += 1
    