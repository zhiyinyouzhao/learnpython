
'''
    一，基本的列表推导式使用方式
'''
# 假设我们想创建一个平方列表

#使用普通方式
varlist = []
for i in range(10):
    varlist.append(i**2)
print(varlist)

#使用map
res = list(map(lambda x:x**2,range(10)))
print(res)

#使用列表推导式

varlist1 = [i**2 for i in range(10)]
print(varlist1)


# '1234' ==> [2,4,6,8]
varstr = '1234'
varlist2 = [int(i)*2 for i in varstr]
print(varlist2)

'''
    二，带有判断条件的列表推导式
    变量 = [变量或变量处理结果 for i in 容器数据类型 条件表达式]
'''

#0-9 求所有的偶数 ==> []
newlist = [i for i in range(10) if i%2==0]
print(newlist)

'''
    三，带有条件判断的多循环列表推导式
    变量 = [变量或变量处理结果 for i in 容器数据类型 条件表达式]
'''

#[1,2,3],[3,1,4] ==> 把两个列表中的元素，两两组合，要求组合的元素不能重复

newlist = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(newlist)