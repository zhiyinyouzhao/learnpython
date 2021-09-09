
'''
1.__len__
    触发机制：当使用len函数去检测当前对象的时候自动触发
    作用： 可以使用len函数检测当前对象中某个数据的信息
    参数： 一个self，接受当前对象
    返回值：必须有，并且必须是一个整型
    注意事项：len要获取什么属性的值，就在返回值中返回哪个属性的长度即可

2.__str__
    触发机制：当使用str或者print函数对对象操作时自动触发
    作用： 代替对象进行字符串的返回，可以自定义打印的信息
    参数： 一个self，接受当前对象
    返回值：必须有，并且必须是一个字符串类型
    注意事项：无

3.__repr__
    触发机制：当使用repr方法对当前对象进行转换时自动触发
    作用： 可以设置repr函数操作对象的结果
    参数： 一个self，接受当前对象
    返回值：必须有，并且必须是一个字符串类型
    注意事项：正常情况下，如果没有__str__,__repr__就会代替__str__

4.__bool__
    触发机制：当使用bool函数转换当前对象时，自动触发，默认情况下，对象转化为了True
    作用： 可以代替对象进行bool类型的转换，可以转换任何数据
    参数： 一个self，接受当前对象
    返回值：必须有，并且必须是一个布尔类型
    注意事项：无
'''



class Demo():
    listurl = [1,2,3]

    # 可以代替对象使用len函数，并返回一个指定的整形
    def __len__(self):
        return len(self.listurl)

    # 可以代替对象进行str或者print的字符串信息返回
    def __str__(self):
        return '<这是当前脚本中的一个对象 str>'


    def __repr__(self):
        return '<这是一个对象 repr>'


    def __bool__(self):
        return  bool(self.listurl)

if __name__ == '__main__':
    obj = Demo()
    # print(len(obj))

    # print(str(obj))
    # print(obj)

    # res = repr(obj)
    # print(res)

    res = bool(obj)
    print(res)