


class Demo():
    '''
    此处是类的文档说明
    '''

    name = 'a'
    age = 20
    def say(self):
        print('会唱会说会rap...')



if __name__ == '__main__':
    obj = Demo()
    # 获取类/对象的所属成员
    res = Demo.__dict__
    res1 = obj.__dict__
    print(res)
    print(res1)
    # 获取类名称组成的字符串
    res2 = Demo.__name__
    print(res2)
    # 获取当前类所在文件的名称，如果是当前文件，显示为__main__
    res3 = Demo.__module__
    print(res3)
    # 获取当前类的父类列表
    res4 = Demo.__bases__
