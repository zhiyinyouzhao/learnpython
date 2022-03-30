


class F():

    def eat(self):
        print('大口喝酒，大口吃肉')


class M():
    def eat(self):
        print('动作优雅，浅尝辄止')


class C(M,F):
    def eat(self):
        super().eat()
        print('吃哭，不吃也哭')


if __name__ == '__main__':
    c = C()
    print(C.mro())
    c.eat()