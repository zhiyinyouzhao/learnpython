
'''
封装的级别
                公有的public           受保护的protected           私有的private
在类的内部       ok                      ok                          ok
在类的外部       ok                      No（python可以）             No

成员:公有的
_成员 :受保护的（约定俗称，python没有实现）
__成员:私有的(可以使用特殊语法获取)

了解即可：
在python中给成员进行私有化，其实就是改了成员的名字
私有化 ==》 _类名__成员
'''



class Person():
    #成员属性
    name = '姓名'
    _age = '年龄'         #受保护的
    __sanwei = '三维'     #私有的

    def __init__(self,n,a,s):
        self.name = n
        self._age = a     #_ :受保护的成员
        self.__sanwei = s  #__:私有成员

    #成员方法
    def say(self):
        print('聊聊人生和理想。。。')

    def sing(self):
        print('高歌一曲，豪放一生。。。')

    def kiss(self):
        print("打个kiss。。。。")

if __name__ == '__main__':
    ym = Person('杨幂',28,'70 50 60')
    # print(ym.__dict__)    #可以获取当前对象的所有成员信息
    # print(Person.__dict__) #可以获取当前类的所有成员信息
    print("=========================")
    print(ym.name)
    print(ym._age)
    # print(ym.__sanwei)

    # print(ym._age)  #在类的外部不能操作，受保护的成员，但python可以
    # ym.kiss()