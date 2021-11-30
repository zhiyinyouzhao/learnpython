

varlist = ['刘德华','张学友','张国荣','黎明','郭富城','小沈阳','刘能','宋小宝','赵四']


'''
    1. len()  检测当前列表的长度
    2. count()  检测当前列表中元素出现的次数
    3. append() 向列表的尾部追加新的元素，返回值为None
    4. insert() 向列表中指定的索引位置添加新的元素
    5. pop()    可以对指定索引位置上的元素出栈操作，返回出栈元素
    6. remove() 可以指定列表重点元素，进行删除,只删除第一个，没有找到，则报错，返回值为None
    7. index()  可以查找指定元素在列表中第一次出现的位置
    8. extend() 接收一个容器类型的数据，把容器中的元素追加到元列表中
    9. clear()  清空列表内容
    10.reverse()    列表反转

'''

# print(varlist.count('张学友'))
#
# res = varlist.append('川哥')
# print(res)
#
# varlist.insert(20,'aa')
# print(varlist)
# res1 = varlist.pop()
# print(res1)
print(varlist)
# varlist.remove('刘德华')
# print(varlist)
res = varlist.index('刘德华',0,4)           #可以在指定索引范围内查找元素的索引位置
print(res)
res1 = varlist.clear()
print(res1,varlist)