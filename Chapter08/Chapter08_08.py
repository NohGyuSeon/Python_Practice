# num = int(input("정수입력 --> "))

# b = bin(num)
# o = oct(num)
# h = hex(num)

# print(num)
# print(b)
# print(o)
# print(h)

value = int(input("정수입력 --> "))

# 접두어 포함
# b = format(value, '#b')
# o = format(value, '#o')
# h = format(value, '#x')

b = format(value, 'b')
o = format(value, 'o')
h = format(value, 'x')

print("10진수: ", value)
print("02진수: ", b)
print("08진수: ", o)
print("16진수: ", h)
