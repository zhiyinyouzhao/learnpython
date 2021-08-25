
'''
1类也是对象，type创建类的类
'''

'''
元类是创建类的类，对象<-class(对称)<-type
'''

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        #生产类的过程委托给父类type
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "user"

#python中类的实例化过程，会首先寻找metacalss，通过metaclass去创建user类
'''

'''

def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return "company"
        return Company

def say(self):
    return 'i am user'

class BaseClass:
    def answer(self):
        return "i am baseclass"

if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)
    #--------------------------------------
    # type 动态创建类
    # User = type("user", (BaseClass,), {"name":"user","say":say})
    # my_obj = User()
    # print(my_obj.answer())
    # --------------------------------------

    my_obj = User("bobby")
    print(my_obj)