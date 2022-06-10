fp = open(r"C:\\NGS\\score.txt", "r")

for line in fp.readlines():
    print(line, end="")
    
fp.close()
