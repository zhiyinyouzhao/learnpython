

'''
    map(func,*iterables)
    功能:
        对传入的可迭代数据中的每个元素放入到函数中进行处理，返回一个新的迭代器
    参数：
        func ：自定义函数or内置函数
        iterables：可迭代数据
    返回值：迭代器
'''

varlist = ['1','2','3','4']
newlist = []

l = [1,2,3,4]
if __name__ == '__main__':
    res = map(str,varlist)
    print(list(res))

    res1 = map(lambda x:x**2,l)
    print(list(res1))
