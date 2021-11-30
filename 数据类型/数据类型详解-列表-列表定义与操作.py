
varlist1 = [1,2,3,4]
varlist2 = ['a','b','b','b']



# 列表拼接
res = varlist1 + varlist2
print(res)
# 列表相乘
res1 = varlist1 * 3
print(res1)
#检测元素是否存在于列表
res3 = 'a' in varlist1
# 索引操作
'''
    0     1    2     3
    ’a‘  'b'   'c'    'd'
    -4    -3   -2    -1
'''
# 追加元素
varlist1.append('ff')
# 删除元素
del varlist2[2]
varlist2.pop()  # 弹出最后一个元素

