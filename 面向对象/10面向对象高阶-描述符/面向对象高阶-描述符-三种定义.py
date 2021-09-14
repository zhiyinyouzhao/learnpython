

#格式一
class scoreManager():
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
class Student():
    score = scoreManager()


#格式二
class Student():

    #在当前需要被管理的类中，直接定义类似下面的三个方法，第一个对应__get__,第二个对应__set__,第三个对应__delete__
    def getscore(self):
        pass
    def setscore(self,value):
        pass
    def delscore(self):
        pass
    #在函数中指定对应的三个方法
    score = property(getscore,setscore,delscore)

#格式三 使用@property装饰器实现
class Student():
    __score = None
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        self.__score = value
    @score.deleter
    def score(self):
        del self.__score