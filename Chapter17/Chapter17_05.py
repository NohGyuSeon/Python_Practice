fp = open(r"C:\\NGS\\gugu_all.txt", "w")

for i in range(2, 10, 1):
    fp.write("\n구구단 %d단 출력\n" % i)
    for k in range(1, 10, 1):
        fp.write("%d x %d = %d\n" % (i, k, (i*k)))
    
fp.close()
