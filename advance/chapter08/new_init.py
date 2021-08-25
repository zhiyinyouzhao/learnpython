

class User:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)
    def __init__(self,name):
        print('in init')
        self.name = name

'''
1.new 是用来控制对象的生产过程，在对象生成之前
2.init是用来完善对象的
3.如果new方法不返回对象，则不会调用init函数
'''

if __name__ == '__main__':
    user = User(name="bobby")