string = "Hello Python"
code = ""

for c in string:
    num = ord(c)
    code += chr(num+10)

print(code)
