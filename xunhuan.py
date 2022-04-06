num = 1
while num <10:
    print(num)
    num += 1

list1 = ['吃饭', '睡觉', '打豆豆']
for v in list1:
    print(v)

# //break 语句  与 continue 的区别
for v in list1:
    if v == '睡觉':
        break
    print(v)

# //break 语句  与 continue 的区别
for v in list1:
    if v == '睡觉':
        continue
    print(v)