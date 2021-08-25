
'''
当看见一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也叫鸭子，那么这只鸟就可以被称为鸭子
'''

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print("Dog is running...")

    def eat(self):
        print("Eating meat...")


class Cat(Animal):
    def run(self):
        print("Cat is running...")


def run_twice(a):
    a.run()
    a.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('Start...')


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    run_twice(Tortoise())
    run_twice(Timer())