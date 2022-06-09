try:
    h, m, s = map(int, input().split(":"))

    if h < 8:
        fra_h = 24 + (h - 8)
    else:
        fra_h = h - 8

    if 0 <= h <= 24 and 0 <= m < 60 and 0 <= s < 60:
        print("KST - ", end="")
        print("{0:02d}".format(h), end=":") 
        print("{0:02d}".format(m), end=":") 
        print("{0:02d}".format(s), end=" / ") 
        print("CET - ", end="")
        print("{0:02d}".format(fra_h), end=":") 
        print("{0:02d}".format(m), end=":") 
        print("{0:02d}".format(s), end="") 
    else:
        raise Exception

except:
    print("Wrong input")

# h, m, s = map(int, input().split(":"))

# if h < 8:
#     fra_h = 24 + (h-8)
# else:
#     fra_h = h - 8

# if 0 <= h <= 24 and 0 <= m < 60 and 0 <= s < 60:
#     print("KST - %02d:%02d:%02d / " % (h, m, s) , end="")
#     print("CET - %02d:%02d:%02d / " % (fra_h, m, s))
# else:
#     print("Wrong input")
