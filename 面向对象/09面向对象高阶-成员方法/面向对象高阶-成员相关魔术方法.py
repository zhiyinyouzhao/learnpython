
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
    注意事项：当存在__getattribute__方法时，会先执行__getattribute__方法
            也要注意，不要在当前的方法中再次去访问这个不存在的成员，会触发递归

3.__setattr__
    触发机制：当给对象的成员进行赋值操作时会自动触发
    作用： 可以限制或管理对象成员的添加和修改操作
    参数： 1.self接受对象，2.key设置的成员名，3.value设置的成员值
    返回值：无
    注意事项：在当前的魔术方法中禁止给当前对象的成员直接进行赋值操作，会触发递归操作
            如果想要给当前成员赋值，需要借助object
            格式：object.__setattr__(self,key,value)

4.__delattr__
    触发机制：当删除对象成员时自动触发
    作用： 可以限制对象成员的删除，还可以删除不存在成员时防止报错
    参数： 1.self接受对象，2.item删除的成员名称
    返回值：无
    注意事项：在当前的魔术方法中禁止直接删除对象的成员，会触发递归操作
            如果想要删除当前对象的成员，需要借助object
            格式：object.__delattr__(self,item)
'''


class Person():
    name = '名字'
    age = '年龄'
    sex = '性别'

    def __init__(self,n,a,s):
        print("触发__init__方法")
        self.name = n
        print("1111111111111111")
        self.age = a
        print("222222222222222222")
        self.sex = s
        print("3333333333333333")

    def say(self):
        print('聊聊人生，谈谈理想')

    def sing(self):
        print('高歌一曲')

    #获取对象成员时自动触发
    def __getattribute__(self, item):
        print('__getattribute__:%s' %item)
        #在方法中使用object来获取属性值
        res = object.__getattribute__(self,item)
        #在方法中可以对访问的成员数据进行处理
        return res[0]+'*'+res[-1]

    #当访问对象中不存在的成员时，自动触发
    def __getattr__(self, item):
        print('__getattr__:%s' %item)

    #给对象的成员进行赋值操作时会自动触发,注意该方法中如果没有给对象进行赋值，那么对象成员赋值失败
    def __setattr__(self, key, value):
        print('__setattr__:%s,%s' %(key,value))
        #object.__setattr__(self, key, value)

    #当删除对象成员时自动触发
    def __delattr__(self, item):
        print('__delattr__:%s' % item)

if __name__ == '__main__':
    zs = Person('张三丰',120,'男')
    # print(zs.name)
    # print("=================")
    # print(zs.a)
    print("=================")
    zs.abc = 'aabbc'
    print('----------------')
    print(zs.abc)
    print("=================")
    # del zs.name
    # print(zs.name)
