


class Outer():
    def newinner(func):
        Outer.func = func               #把传递进来的函数定义为类方法
        return Outer.inner              #同时返回一个新的绑定类方法

    def inner():
        print('拿到妹子的微信')
        Outer.func()
        print('看一场午夜电影')




#@Outer.newinner                     #Outer.newinner(love) ==> Outer.inner
def love():
    print('和妹子谈谈人生喝喝茶...')


if __name__ == '__main__':
    #love()
    love = Outer.newinner(love)
    love()