

from chapter04.class_method import Date

class User:
    def __init__(self,birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2021-self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1990,2,1))
    print(user.__birthday)
    print(user._User__birthday)
    print(user.get_age())