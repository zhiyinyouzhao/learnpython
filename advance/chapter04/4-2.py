
'''
抽象基类
'''

from collections.abc import Sized
# 我们去检查某个类是否有某个方法

class Company(object):
    def __init__(self,employ_list):
        self.employee = employ_list


    def __len__(self):
        return len(self.employee)


if __name__ == '__main__':
    com = Company(["bobby1","bobby2"])
    print(len(com))
    print(hasattr(com,'__len__'))
    # 我们在某些情况下希望判定某个对象的类型
    print(isinstance(com,Sized))
    from collections.abc import Sized
    # 我们需要强制某个子类必须实现某些方法
    # 实现一个web框架，集成cache(redis,cache,memorycache)
    # 需要设计一个抽象基类，指定子类必须实现某些方法

    # 如何去模拟一个抽象基类
    # class CacheBase():
    #     def get(self,key):
    #         raise NotImplementedError
    #     def set(self,key,value):
    #         raise NotImplementedError
    #
    # class RedisCache(CacheBase):
    #     pass
    #
    # redis_cache = RedisCache()
    # redis_cache.set("key","value")
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

    redis_cache = RedisCache()
    redis_cache.set("key","value")