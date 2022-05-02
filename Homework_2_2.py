data = input().split()

if data[1] == '+':
    print('%.5f' % (float(data[0]) + float(data[2])))
elif data[1] == '-':
    print('%.5f' % (float(data[0]) - float(data[2])))
elif data[1] == '*':
    print('%.5f' % (float(data[0]) * float(data[2])))
elif data[1] == '/':
    if data[2] == '0':
        print("NaN") 
    else:
        print('%.5f' % (float(data[0]) / float(data[2])))
elif data[1] == '%':
    print('%.5f' % (float(data[0]) % float(data[2])))
    