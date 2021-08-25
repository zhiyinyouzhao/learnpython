
'''
多态和鸭子类型，当看见一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也叫鸭子，那么这只鸟就可以被称为鸭子
'''

'''
java 里必须要继承父类，然后重写say方法
python class里都必须要实现say方法
'''
class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a dog")

class Duck(object):
    def say(self):
        print("i am a Duck")




if __name__ == '__main__':
    # animal = Cat
    # animal().say()
    animal_list = [Cat,Dog,Duck]
    for animal in animal_list:
        animal().say()

