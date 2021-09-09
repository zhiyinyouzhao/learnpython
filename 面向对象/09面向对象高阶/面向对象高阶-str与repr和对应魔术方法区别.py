
'''
认识str和repr区别：
    1.str和repr函数能够把其他类型的数据转为字符串类型
    2.str函数会把对象转为更适合人类阅读的形式，repr函数会把对象转为解释器读取的形式
    3.如果数据对象并没有更明显的区别的话，str和repr的结果是一样的
'''


class Demo():
    # def __str__(self):
    #     return '123'
    #
    # def __repr__(self):
    #     return '123'
    pass


if __name__ == '__main__':
    obj =Demo()
    r1 = str(obj)
    r2 = str(obj)
    print(r1,type(r1))
    print(r2,type(r2))