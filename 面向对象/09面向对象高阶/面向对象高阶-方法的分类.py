

'''
1.对象方法
    特征； 1.在类中定义的方法，含义self参数
          2.还有self的方法，只能使用对象调用
          3.该方法会把调用的对象传递进来

2.类方法
    特征:  1.在类中定义的方法，使用装饰器@classmethod进行装饰
          2.方法中有cls这叫个形参
          3.不需要实例化对象，直接使用类进行调用
          4.会把调用这个方法的类传递进来

3.绑定类方法
    特征： 1.在类中定义的方法，没有任何参数
          2.只能使用类进行调用
          3.不会传递任何参数进来

4.静态方法
    特征： 1.在类中定义的方法，没有任何参数
          2.使用了@staticmethod进行了装饰
          3.可以使用对象或者类调用
          4.不会传递对象或者类进来
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
    def func3():
        print('this is bind class function func3')


    # 静态方法
    @staticmethod
    def func4():
        print('this is static method function func4')

if __name__ == '__main__':
    #类方法
    # obj = Demo()
    # Demo.func1('a')  # 不推荐直接使用类调用对象方法
    #对象方法
    # obj1 = Demo()
    # Demo.func2()        #可以使用类直接调用
    # obj1.func2()        #即便使用对象进行调用，传递进去的依然是类
    #绑定类方法
    # obj3 = Demo()
    # Demo.func3()        #可以使用类调用绑定类方法
    # obj3.func3()        #不能使用对象调用绑定类方法
    # 静态方法
    obj4 = Demo()
    Demo.func4()            # 可以使用类调用绑定类方法
    obj4.func4()            #可以使用对象调用绑定类方法