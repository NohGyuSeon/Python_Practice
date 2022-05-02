data = input().split()
n = int(data[0]) # 피보나치 수열의 최대 값
k = int(data[1]) # 피보나치 수열의 index 값

def fibo(n, k):
    count = k
    result_count = count
    bool = False
    f = [1, 1]
    i = 2
    while True:
        f.append(f[i-2] + f[i-1])
        if f[i-1] > n:
            if i-1 > k:
                break
            else:
                i += 1
                result_count -= 1
                bool = True
        else:
            i += 1
            
    if bool:
        return f[result_count], f[k-1]
    else:
        return f[i-2], f[k-1] 

x, y = fibo(n, k)

print(x, y)
