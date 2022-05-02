t1 = input("input string: ")
t1_update = t1.upper()
len = len(t1)

print("전체문자 개수: %d글자" % len)
print("문자 A 개수: %d개" % t1_update.count("A"))
print("문자 O 개수: %d개" % t1_update.count("O"))
