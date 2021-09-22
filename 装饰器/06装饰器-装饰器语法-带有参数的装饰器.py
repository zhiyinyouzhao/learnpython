



# 如果你的装饰器需要有参数，那么给装饰器一个壳，用于接收装饰器的参数
def kuozhan(var):
    def outer(f):
        def inner1():
            print('妹子给了你微信')
            f()
        def inner2():
            print('妹子给介绍了个大妈')
            f()
        if var == '高富帅':
            return inner1
        else:
            return inner2
    return outer


@kuozhan('高富帅')
def love():
    print('谈谈人生')

if __name__ == '__main__':
    a = kuozhan('高富帅')
    # love()      #kuozhan(var) ==》 outer() ==> outer(love) ==> inner()
    b = a(love)
    # print(b)
    b()