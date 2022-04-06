man = {'height':180,'姓名':'星仔','work':'程序员','sport':'6KM'}
print(man)
print(man['work'])

man['work'] = '滴滴司机'
print(man['work'])
man['钱'] = '100万'
print(man)

man.pop('sport')
print(man)
print(man['名字'])