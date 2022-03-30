
'''
认识str和repr区别：
    1.str和repr函数能够把其他类型的数据转为字符串类型
    2.str函数会把对象转为更适合人类阅读的形式，repr函数会把对象转为解释器读取的形式
    3.如果数据对象并没有更明显的区别的话，str和repr的结果是一样的
'''


class Demo():
    def __str__(self):
        print("111111111")
        return '123'

    def __repr__(self):
        print("2222222222")
        return '123'



if __name__ == '__main__':
    # num = 521
    # r1 = str(num)
    # r2 = repr(num)
    # print(r1,type(r1))
    # print(r2,type(r2))
    # print("==================")
    #
    # s = '521'
    # r1 = str(s)
    # r2 = repr(s)
    # print(r1,type(r1))
    # print(r2,type(r2))
    # print("==================")

    obj =Demo()
    print("3333333333333")
    r1 = str(obj)
    print("444444444444")
    r2 = repr(obj)
    print("55555555555")
    print(r1,type(r1))
    print(r2,type(r2))