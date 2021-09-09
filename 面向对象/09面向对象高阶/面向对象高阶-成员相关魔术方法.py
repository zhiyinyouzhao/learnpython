
#成员相关魔术方法
'''
1.__getattribute__
    触发机制：当使用len函数去检测当前对象的时候自动触发
    作用： 可以使用len函数检测当前对象中某个数据的信息
    参数： 一个self，接受当前对象
    返回值：必须有，并且必须是一个整型
    注意事项：len要获取什么属性的值，就在返回值中返回哪个属性的长度即可
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

    def __getattribute__(self, item):


if __name__ == '__main__':
    zs = Person('张三丰',120,'男')
    print(zs.name)
