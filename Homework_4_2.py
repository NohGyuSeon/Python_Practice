A, B, n = map(int, input().split())
sum = []
res = 0

for i in range(A, B):
    if i % n == 0:
        sum.append(i)

for i in range(len(sum)):
    res += sum[i]

print("%.2f" % (res / len(sum)))
