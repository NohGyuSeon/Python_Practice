import math as m

fp = open(r"C:\\NGS\\radian.txt", "w")

for i in range(0, 361, 10):
    fp.write("\nsine 값 계산: %f\n" % m.sin(m.radians(i)))
    
fp.close()
