

"""
生成器解决了资源消耗的问题，用一个值，产生一个值，用完就扔
"""

"""
yield和return类似，return expression 直接退出函数（方法），并返回expression
yield 也返回值，但返回的是一个generator，generator当前的值就是yield后面跟的表达式的值
"""

#输出不大于10的所以偶数
#不使用生成器
# def generator_even(max):
#     l = []
#     for i in range(max+1):
#         if i % 2 == 0:
#             l.appen(i)
#     return l
#使用生成器
def generator_even(max):
    print('1111111111')
    for i in range(max+1):
        if i % 2 == 0:
            yield i

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


if __name__ == '__main__':
    # even = generator_even(10)
    # print('222222222222')
    # for n in even:
    #     print(n,end=' ')

    o = odd()
    print(next(o))
    # for i in o:
    #     print(i)


