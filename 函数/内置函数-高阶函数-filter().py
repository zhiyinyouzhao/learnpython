from collections.abc import Iterator, Iterable

'''
    filter(func,iterable)
    功能：
        过滤数据，把iterable中的每个元素拿到func函数中进行处理、
        如果函数返回True则保留这个数据，返回False则丢弃这个数据
    参数:
        func 自定义函数
        iterable 可迭代的数据
    返回值：
        保留下来的数据组成的迭代器
'''


#要求保留所有的偶数，丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9]

def myfunc(n):
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    res = filter(myfunc,varlist)
    print(type(res),isinstance(res,Iterator))
    print(list(res),type(res))
    it = filter(lambda x: True if x % 2 ==0 else False,varlist)
    print(list(it),type(it))
