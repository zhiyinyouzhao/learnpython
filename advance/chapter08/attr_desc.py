
from datetime import date,datetime

'''
如果user是某个类的实例，那么user.age(已经等价的getattr（user，‘age’)
首先调用__getattribute__。如果类定义了__getattr__方法。
那么在__getattribute__抛出Attribute的时候就会调用到__getattr__。
而对于描述符（__get__）的调用，则是发生在__getattribute__内部的。
user = User()，那么user.age顺序如下:
1.如果age是出现在User或其他基类的__dict__中，且age是data descriptor，那么调用其__get__方法
2，如果age是出现在user的__dict__中，且age是data descriptor，那么直接返回user.__dict__['age'],否则
3，如果age是出现在User或其他基类的__dict__中:
    3.1 如果age是Non-data descriptor，那么调用其__get__方法，否则
    3.2 返回__dict__['age']
4.如果User有__getattr__方法，调用__getattr__方法，否则
5.抛出AttributeError
'''
import numbers


# 数据属性描述符
class IntField:
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
