
#描述符类
class PersonName():
    print("333333333333333")
    __name = 'abc'

    def __get__(self, instance, owner):
        print('__get__')
        print(self,instance,owner)
        return self.__name

    def __set__(self, instance, value):
        print('__set__')
        print(self, instance, value)
        self.__name = value

    def __delete__(self, instance):
        print('__delete__')
        print(self, instance)


#普通类
class Person():
    print("111111111111")
    #把类中的一个成员属性交给一个描述符类来实现
    name = PersonName()
    print("22222222222")


if __name__ == '__main__':
    zs = Person()
    print(zs.name)
    print("=================")
    zs.name = '张三'
    print(zs.name)
    print("=================")
    del zs.name
    print(zs.name)
