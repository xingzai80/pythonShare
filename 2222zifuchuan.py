var1 = 'Hello World!'
print(var1)
print('长度',len(var1))

var2 = "你好 帅气星仔"
print(var2)
print(var1[1:5])
print(var2[1:7])

var3 = var1 + var2
print(var3)

isHaveMoney = "有钱" in var3
print(isHaveMoney)

isHandsome = "帅" in var3
print(isHandsome)


print("我是 %s ,今年 %d 岁" % ('星仔', 18))