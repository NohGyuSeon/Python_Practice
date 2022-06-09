tu_test = ()
list_test = list(tu_test)
    
for i in range(10, 101, 10):
    list_test.append(i)

tu_test = tuple(list_test)

for i in range(len(tu_test)):
    print(tu_test[i])

# print(type(tu_test))
