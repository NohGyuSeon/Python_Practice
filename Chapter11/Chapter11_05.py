import time

for i in range(1, 11, 1):
    if i < 10:
        print("숫자", i, end=", ")
    else:
        print("숫자", i)
    time.sleep(1)
    
