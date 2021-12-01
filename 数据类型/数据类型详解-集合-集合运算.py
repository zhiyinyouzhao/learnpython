

'''
    集合的主要运算
        交集  & set.intersection() set.intersection_update()
        并集  | union()   update()
        差集  - set.difference(),set.difference_update()
        对称差集    ^   set.symmetric_difference(),set.symmetric_difference_update()
'''

vars1 = {'郭富城','刘德华','张学友','黎明','都敏俊'}
vars2 = {'尼古拉斯赵四','刘能','小沈阳','宋小宝','都敏俊'}

# 求两个集合相交的部分
# res = vars1 & vars2
# print(res)
#交集运算函数

# res = vars1.intersection(vars2) # 返回交集的结果，新的集合
# print(res)
# res = vars1.intersection_update(vars2) # 计算2个集合的相交部分，计算结果重新复制给第一个集合，没有返回值
# print(res)

#求两个集合的并集，就是把集合中所有元素集中起来（去除重复）
# res1 = vars1 | vars2
# print(res1)
# res1 = vars1.union(vars2)   #返回并集结果，新的集合
# print(res1)
# res1 = vars1.update(vars2)  #没有返回值，把结果重新赋值给第一个集合
# print(res1)
# print(vars1)

#差集运算
# res3 = vars1 - vars2 # vars1有，而vars2没有的
# print(res3)
# set.difference(),set.difference_update() 同上

# 对称差集,去除相同的元素，返回不同的元素
# res4 = vars1 ^ vars2
# print(res4)
# set.symmetric_difference(),set.symmetric_difference_update() 同上

# 检测超集，子集
vars3 = {1,2,3,4,5,6,7,8,9}
vars4 = {1,2,3}

#检测是否是超集
res = vars3.issuperset(vars4)
print(res)

#检测是否是子集
res1 = vars3.issubset(vars4)
print(res1)

#检测是否相交
res2 = vars3.isdisjoint(vars4)
print(res2)
