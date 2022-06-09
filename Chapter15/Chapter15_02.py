names = [''] * 5    

for i in range(0, 5, 1):
    n = input()
    names[i] += n
    
names.sort()
for i in range(len(names)):
    print(names[i], end=" ")
    