
'''
多态和鸭子类型
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
    animal = Cat
    animal().say()