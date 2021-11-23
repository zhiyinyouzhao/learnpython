from collections import Iterator, Iterable
'''
    iter()
        功能：把可迭代的对象，转为一个迭代器对象
        参数：可迭代对象（str,list,tuple,dict,set,range）
        返回值：迭代器对象
    注意：迭代器一定是一个可以迭代的对象，但是可迭代对象不一定是迭代器
'''


'''
    迭代器取值特点：
        取出一个少一个，直到都取完，最后再获取就会报错
    迭代器取值方案:
        1.next(),调用一次获取一次，直到数据被取完
        2.list(),使用list函数直接取出迭代器中所有的数据
        3.for 使用for循环遍历迭代器对象
'''

'''
    检测迭代器和可迭代对象的方法
    from collections import Iterator,Iterable
'''


f4 = ['赵四','刘能','小沈阳','海参炒面']


#for循环
for i in f4:
    print(i)

res = iter(f4)
#1.可以把可迭代对象转为迭代器使用，使用next()函数去调用迭代器对象
# r = next(res)
# print(r)

# 2.list
# r = list(res)
# print(r)

# 3.for
for j in res:
    print(j)


varstr = '123456'
res = iter(varstr)

r1 = isinstance(varstr,Iterable)
r2 = isinstance(varstr,Iterator)
r3 = isinstance(res,Iterable)
r4 = isinstance(res,Iterator)
print(r1)
print(r2)
print(r3)
print(r4)

