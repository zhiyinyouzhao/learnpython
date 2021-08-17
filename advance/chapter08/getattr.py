from datetime import date,datetime
#__getattr__,__getattribute__
#__getattr__就是在找不到属性的时候调用
#__getattribute__ 首先进入该函数


class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        return "not find attr"


if __name__ == '__main__':
    user = User("bobby",date(year=1987,month=1,day=1))
    print(user.age)
