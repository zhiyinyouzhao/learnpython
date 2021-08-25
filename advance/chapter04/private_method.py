
'''

'''

from chapter04.class_method import Date

class User:
    def __init__(self,birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2021-self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1990,2,1))
    #私有属性无法通过.获取
    # print(user.__birthday)
    #pytho实际上会把__birthday变形为_classname__attr
    print(user._User__birthday)
    print(user.get_age())