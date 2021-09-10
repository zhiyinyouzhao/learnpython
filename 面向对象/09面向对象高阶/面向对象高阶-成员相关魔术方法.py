
#成员相关魔术方法
'''
1.__getattribute__
    触发机制：当访问对象成员时，自动触发，无论当前成员是否存在
    作用： 可以在获取对象成员时，对数据进行一些处理
    参数： 一个self接受对象，一个item接受当前访问的成员名称
    返回值：可有可无，如果有，返回的值就是访问的结果
    注意事项：在当前的魔术方法中，禁止使用对象.成员的方式进行成员访问，会触发递归。
            如果想要在当前魔术方法中访问对象的成员必须使用object来进行访问
            格式：object.__getattribute__(self,item)


2.__getattr__
    触发机制：当访问对象中不存在的成员时，自动触发
    作用： 防止访问不存在的成员时报错，也可以为不存在的成员进行赋值操作
    参数： 一个self接受对象，一个item接受当前访问的成员名称
    返回值：可有可无，如果有，返回的值就是访问的结果
    注意事项：无
'''


class Person():
    name = '名字'
    age = '年龄'
    sex = '性别'

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s

    def say(self):
        print('聊聊人生，谈谈理想')

    def sing(self):
        print('高歌一曲')

    #获取对象成员时自动触发
    def __getattribute__(self, item):
        print(item)
        #在方法中使用object来获取属性值
        res = object.__getattribute__(self,item)
        #在方法中可以对访问的成员数据进行处理
        return res[0]+'*'+res[-1]

    #当访问对象中不存在的成员时，自动触发
    def __getattr__(self, item):
        print(item)

if __name__ == '__main__':
    zs = Person('张三丰',120,'男')
    print(zs.name)
    print(zs.abc)