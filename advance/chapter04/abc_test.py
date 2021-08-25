
'''
抽象基类abc
1.在基础类设定好方法，所有继承基础类的类中都需要实现该方法覆盖基类方法
2.抽象基类无法实例化
'''

from collections.abc import Sized

class Company(object):
    def __init__(self,employ_list):
        self.employee = employ_list

    def __len__(self):
        return len(self.employee)




if __name__ == '__main__':
    com = Company(['bobby1','bobby2'])
    print(len(com))
    # 应用场景一：我们在某些情况之下希望判定某个对象的类型
    print(isinstance(com,Sized))
    # 应用场景二：我们需要强制某个子类必须实现某些方法
    '''
    例如：实现一个web框架，继承cache（redis，cache，memorychache）
    需要设计一个抽象基类，指定子类必须实现某些方法
    '''
    import abc
    class CacheBase(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def get(self,key):
            pass

        @abc.abstractmethod
        def set(self,key,value):
            pass

    class RedisCache(CacheBase):
        def set(self,key,value):
            pass
        def get(self,key):
            pass

    redis_cache = RedisCache()
    # redis_cache.set("key","value")