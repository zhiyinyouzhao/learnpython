


varlist = ['刘德华','张学友','张国荣','黎明','郭富城','小沈阳','刘能','宋小宝','赵四']


'''
    语法 列表[开始索引:结束索引:步进值]
'''
# 从开始索引到最后
res1 = varlist[2:]
print(res1)
# 从开头到指定的结束索引之前
res2 = varlist[:2]
print(res2)
# 从开始索引到指定结束索引之前
res3 = varlist[2:6]
print(res3)
# 从指定索引开始到指定索引前结束，按照指定的步进进行切片取值
res4 = varlist[2:6:2]
print(res4)
res5 = varlist[:]
print(res5)
res6 = varlist[::]
print(res6)
# 倒着获取列表
res7 = varlist[::-2]
print(res7)



# 使用切片方法，对列表数据进行更新和删除
# 从指定下标开始，到指定下标前结束，并替换为对应的数据（容器类型数据，会拆成每个运算进行赋值）
# varlist[2:6] = 'aa'
varlist[2:6] = ['a','b','c',1,2,3]
print(varlist)