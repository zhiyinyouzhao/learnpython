

'''
self 在类方法中代表当前这个对象，形参
self 代表调用这个方法的对象
self 就可以在类的内部代替对象进行各种操作

如果类中定义的方法不含self这个形参时（self形参，包括其他的代替都不可以）
那么这个方法不能使用对象去调用
不含self形参的方法，只能使用类去调用
这种不接受对象作为形参的方法，叫做绑定类方法
'''

class Person():
    name = '名字'
    age = '年龄'
    sex = '性别'


    def sing(self):
        print('会唱...')

    def dance(self):
        print('会跳...')

    def rap(self):
        print('会rap...')

    def func(self):
        #测试在类的内部是否可以向类外部一样去访问和操作成员
        print(self)
        self.name = '张三三'
        self.rap()
        
    #这种不接受对象作为形参的方法，叫做绑定类方法
    def func2():
        print("我是一个没有self的方法...")


if __name__ == '__main__':
    zs = Person()
    print(zs.name)
    print(zs)
    print("==================")
    zs.func()
<<<<<<< HEAD
    # print(zs.name)
    # print(Person.name)
    # print(Person.func2())
=======
    print("-------------")
    print(zs.name)
    print(Person.name)
    print(Person.func2())
>>>>>>> cf93a1682ccf85a8fa07071a1cb416361b68df67
