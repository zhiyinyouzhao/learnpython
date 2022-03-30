
'''
        HuMan
    F           M
        C
'''


class HuMan():
    num = 444
    def eat(self):
        print('顿顿都是小烧烤')


class F(HuMan):
    num = 333
    def eat(self):
        super().eat()
        print(super().num)
        print('大口喝酒，大口吃肉')


class M(HuMan):
    num = 222
    def eat(self):
        super().eat()
        print(super().num)
        print('动作优雅，浅尝辄止')


class C(F,M):
    num = 111
    def eat(self):
        super().eat()
        print(super().num)
        print('吃哭，不吃也哭')

if __name__ == '__main__':
    c = C()
<<<<<<< HEAD
    '''
    C->F->M->HuMan
=======
    c.eat()

    '''
        顿顿都是小烧烤
        444
        动作优雅，浅尝辄止
        222
        大口喝酒，大口吃肉
        333
        吃哭，不吃也哭
        
        
        
    '''
    '''
    C->F->M->H
    [<class '__main__.C'>, <class '__main__.F'>, <class '__main__.M'>, <class '__main__.HuMan'>, <class 'object'>]
>>>>>>> cf93a1682ccf85a8fa07071a1cb416361b68df67
    '''
    print(C.mro())
    c.eat() #''顿顿都是小烧烤''-444-'动作优雅，浅尝辄止'-222--'大口喝酒，大口吃肉'-33333333-'吃哭，不吃也哭'