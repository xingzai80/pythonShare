list1 = ['吃饭', '睡觉', '打豆豆']
print(len(list1)) #打印长度
print(list1[0])
list1[0] = '干饭'
print(list1[2])
# print(list1[5])
list1.append("抽烟")
list1.append("喝酒")
list1.append("烫头")
del list1[1]
print(list1)
print(list1[2:4])

list2 = ['搬砖','挣钱']
list3 = list1 + list2
print(list3)

# for v:= range list1:
#     print(v)
#