# import sys

# n = int(sys.stdin.readline())

n = int(input())

bin = format(n, '#b')
bin_array = format(n, 'b')
# bin_count = 0

# for i in range(0, len(bin_array)):
#     if(bin_array[i] == '1'):
#         bin_count += 1

def soultion(n, q):
    rev_base = ''
    val = n
    n = abs(n)

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    if(val > 0):
        return rev_base[::-1]
    elif(val == 0):
        return '0'
    else:
         return '-' + rev_base[::-1]

tri = soultion(n, 3)
# tri_count = 0

# for i in range(0, len(tri)):
#     if(tri[i] == '2'):
#         tri_count += 1

print(bin, bin.count("1"), '/', tri, tri.count("2"), end=" ")
