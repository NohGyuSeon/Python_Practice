line, start, add = map(int, input().split())

# str = []
# for i in range(1, start+1):
#     str += '*'

# if add > 0:
#     for i in range(0, line):
#         print('*'*start, end='')
#         for j in range(0, i):
#             if(i != 0):
#                 print('*'*add, end='')
#         print()
# else:
#     for i in range(line, 0, -1):
#         if (i != line):
#             for j in range(abs(add)):
#                 if (not str):
#                     str.clear
#                     break
#                 else:
#                     str.pop()
#         print(''.join(str))

for i in range(line):
    for n in range(start + add*i):
        print('*', end="")
    print()
    