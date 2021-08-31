




class Person():
    name = None
    age = None
    sex = None

    #__init__
    def __init__(self,n,a,s):
        print("我是一个初始化方法")
        self.name = n
        self.age = a
        self.sex = s

    def say(self):
        print("大家好")


if __name__ == '__main__':
    zzh = Person("渣渣辉",56,'男')
    print(zzh.name)