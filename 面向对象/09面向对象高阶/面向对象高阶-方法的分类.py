

'''
1.对象方法
    特征； 1.在类中定义的方法，含义self参数
          2.还有self的方法，只能使用对象调用
          3.该方法会把调用

2.类方法
    特征:  1.在类中定义的方法，使用装饰器@classmethod进行装饰
          2.方法中有cls这叫个形参
          3.不需要实例化对象，直接使用类进行调用
          4.会把调用这个方法的类传递进来

3.绑定类方法
    特征： 1.在类中定义的方法，没有任何参数
          2.只能使用
'''


class Demo():

    # 对象方法
    def func1(self):
        print(self)
        print('this is object function func1')

    #类方法
    @classmethod
    def func2(cls):
        print(cls)
        print('this is class function func2')

    # 绑定类方法
    def func3(self):
        print('this is bind class function func3')

if __name__ == '__main__':
    #类方法
    # obj = Demo()
    # Demo.func1('a')  # 不推荐直接使用类调用对象方法
    #对象方法
    # obj1 = Demo()
    # Demo.func2()        #可以使用类直接调用
    # obj1.func2()        #即便使用对象进行调用，传递进去的依然是类
    #绑定类方法
    obj3 = Demo()
    Demo.func3()
    obj3.func3()
