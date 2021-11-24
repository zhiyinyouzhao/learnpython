
from functools import reduce

'''
   reduce(func,*iterable)
   功能:
        每一次从iterable拿出2个元素，放入到func函数中进行处理，得出一个计算结果
        然后把这个计算结果和iterable中的第三个元素，放入到func函数中继续运算
        得出的结果和之后的第四个元素，加入到func函数中进行处理，以此内推，直到最后的元素都参与运算
    参数：
        func: 内置函数or自定义函数
        iterable：可迭代的数据
    返回值:
        最终运算结果
'''

varlist = [5,2,1,1]  # ==> 5211
def func(x,y):
    return x*10 + y
# 字符串‘456’ ==> 456

s = '456'
def func1(x,y):
    return int(x)*10 + int(y)


if __name__ == '__main__':
    res = reduce(func,varlist)
    print(res,type(res))

    res1 = reduce(func1,s)
    print(res1, type(res1))