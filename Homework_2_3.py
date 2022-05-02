data = input().split()

n1 = int(data[0])
n2 = int(data[1])

def GCD(n1, n2):
    while True:
        if n1 <= 0 or n2 <= 0:
            break
        if n1 == n2:
            gcd = n1
            break
        else:
            if n1 > n2:
                n1 = n1 - n2
            else:
                n2 = n2 - n1
    return gcd

n1 = int(data[0])
n2 = int(data[1])

def LCM(x, y):
    result = (n1*n2)//GCD(n1, n2)
    return result

if n1 <= 0 or n2 <= 0:
    print("Wrong input")
else:
    print("GCD: %d / LCM: %d" % (GCD(n1, n2), LCM(n1, n2)))
