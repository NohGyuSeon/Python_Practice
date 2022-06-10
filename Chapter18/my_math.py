def sum_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return(sum)

def sum_a_to_b(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return(sum)

def gugu(n):
    for i in range(1, 10, 1):
        print("%d x %d = %d\n" % (n, i, (i*n)))


def gugu_all():
    for i in range(2, 10, 1):
        print("구구단 %d단 출력\n" % i)
        for k in range(1, 10, 1):
            print("%d x %d = %d\n" % (i, k, (i*k)))
        print()
