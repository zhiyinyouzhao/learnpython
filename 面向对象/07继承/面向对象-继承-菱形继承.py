
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
    c.eat()
    '''
    C->F->M->H
    '''
    print(C.mro())