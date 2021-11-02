


class KuoZhan():
    def __call__(self, cls):
        #把接收的类。赋值给当前对象，作为一个属性
        self.cls = cls
        #返回一个函数
        return self.newfunc


    def newfunc(self):
        self.cls.name = '我是在类装饰器中追加的新属性 name'
        self.cls.func2 = self.func2
        # 返回传递进来的类的实例化结果，obj
        return self.cls()

    def func2(self):
        print('我是装饰器中追加新的方法，func2')





#@KuoZhan()                      #KuoZhan() ==> obj  ==> @obj(Demo) ==> __call__() ==> newfunc()
class Demo():
    def func(self):
        print('我是Demo类中定义的func方法')

if __name__ == '__main__':
    # obj = Demo()
    # obj.func()
    # obj.func2()
    obj = KuoZhan()
    demo = obj(Demo)
    print(demo)
    demo().func()
