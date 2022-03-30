

'''

    nonlocal 关键字在局部函数中使用
    在内函数中如果想使用外层函数的变量，那么需要使用nonlocal 关键字引用
'''

# name = 'AAA'
#
#
# def func():
#     name = 'aaa'
#     # if 1:
#     #     name = 100
#     print(name)
#
#
# func()
# print(name)


def outer():
    # 外函数的局部变量
    num = 10
    # 内函数，局部函数，在函数的内部定义的函数
    print(1111)
    def inner():
        print(3333)
        nonlocal num  #可以引用上一层函数中定义的局部变量，但依然不能提升为全局变量
        num += 1
        print(num)

    print(22222)
    inner()
    print(3333333)

if __name__ == '__main__':
    print(4444444)
    outer()