
from datetime import date,datetime

'''
如果user是某个类的实例，那么user.age(已经等价的getattr（user，‘age’)
首先调用__getattribute__。如果类定义了__getattr__方法。
那么在__getattribute__抛出Attribute的时候就会调用到__getattr__。
而对于描述符（__get__）的调用，则是发生在__getattribute__内部的。

'''
import numbers
class IntField:
    #数据描述符
    def __get__(self,instance,owner):
        return  self.value

    def __set__(self,instance,value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("int value need")
        self.value = value

    def __delete__(self,instance):
        pass


class User:
    age = IntField()

# class User:
#     def __init__(self,name,birthday):
#         self.name = name
#         self.birthday = birthday
#         self._age = 0
#
#     # def get_age(self):
#     #     return datetime.now().year-self.birthday.year
#
#     @property
#     def age(self):
#         return datetime.now().year-self.birthday.year
#
#     @age.setter
#     def age(self,value):
#         self._age = value
if __name__ == '__main__':
    user = User()
    user.age = "abc"
    print(user.age)
