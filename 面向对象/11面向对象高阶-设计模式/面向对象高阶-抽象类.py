

import abc
class writeCode(metaclass=abc.ABCMeta):
    #需要抽象的方法，使用装饰器进行装饰
    @abc.abstractmethod
    def write_php(self):
        pass
    def write_java(self):
        print('实现java代码开发')
    def write_python(self):
        print('实现python代码开发')


# 定义子类继承抽象类，并实现抽象类中的抽象方法
class Demo(writeCode):
    def write_php(self):
        print('实现了php代码的开发')

if __name__ == '__main__':
    # obj = writeCode()  含有抽象方法的抽象类不能实例化
    a = Demo()
    print(a)
    a.write_java()
    a.write_php()
    a.write_python()


