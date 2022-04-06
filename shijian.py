import time

print(time.time())


day1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(day1)

day2 = time.strftime("%Y-%m-%d", time.localtime())
print(day2)