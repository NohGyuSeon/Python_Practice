korea = input("Korea time: ").split()
hour = int(korea[0])
minute = int(korea[1])
france_hour = hour - 8
france_minute = minute

if france_hour < 0:
    france_hour = 24 + france_hour
    print("France time: %d %d" % (france_hour, france_minute))
else:
    print("France time: %d %d" % (france_hour, france_minute))
