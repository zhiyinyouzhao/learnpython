



'''
还有一种装饰器，是专门装饰类的。也就是在类的定义的前面使用@装饰器这种语法

@装饰器
class Demo():
    pass

装饰器给函数进行装饰，目的是不改变函数调用和代码的情况下给原函数增加功能

装饰器给类进行装饰，目的是不改变类的定义和调用的情况下给类增加新的成员
'''

# 使用函数装饰器，给类进行装饰，增加新的属性和方法

#定义函数，接受一个类，返回修改后的类
def kuozhan(cls):
    def func2():
        print('我是装饰器中追加新的方法，func2')
    cls.func2 = func2 #把刚才定义的方法赋值给类
    cls.name = '我是在装饰器中追加的新属性 name'
    #返回时，把追加类新成员的类返回去
    return cls


@kuozhan            #kuozhan(Demo) ==> cls ==> Demo
class Demo():
    def func():
        print('我是Demo类中定义的func方法')

if __name__ == '__main__':
    Demo.func() #此时再调用的Demo类是通过装饰器更新过的Demo类
    Demo.func2()