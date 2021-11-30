'''

#简单的copy，就可以把列表复制一份，对新拷贝的列表进行操作，也是独立的
varlist = [1,2,3]

newlist = varlist.copy()

print(varlist,id(varlist))
print(newlist,id(newlist))
'''

# 使用copy，拷贝一个多维列表
varlist1 = [1,2,3,['a','b','c']]
newlist1 = varlist1.copy()
print(varlist1,id(varlist1))
print(newlist1,id(newlist1))


# 如果是一个被拷贝的列表，对它的多维列表元素进行操作时，会导致原列表中的多维列表也发生了变化
del newlist1[3][1]

print(varlist1,id(varlist1))
print(newlist1,id(newlist1))

print(varlist1[3],id(varlist1[3]))
print(newlist1[3],id(newlist1[3]))

'''
    通过id检测，发现列表中的多维列表是同一个元素（对象）
['a', 'c'] 2447264787648
['a', 'c'] 2447264787648
print(varlist1[3],id(varlist1[3]))
print(newlist1[3],id(newlist1[3]))

'''


'''
    浅拷贝：只能拷贝当前列表，不能拷贝列表中的多维列表元素
    深拷贝：不光拷贝当前列表，同时把列表中的多维元素也拷贝了一份
'''
import copy
varlist2 = [1,2,3,['a','b','c']]
newlist2 = copy.deepcopy(varlist2)

print('===============================')
print(varlist2,id(varlist2))
print(newlist2,id(newlist2))

del newlist2[3][1]

print(varlist2,id(varlist2))
print(newlist2,id(newlist2))

print(varlist2[3],id(varlist2[3]))
print(newlist2[3],id(newlist2[3]))


