


#利用闭包，把函数当作参数传递，并且在函数内去调用传递进来的函数，并返回一个函数

'''
原理
#定义外函数
def outer(f):
    #定义内涵数,并且在内涵数中调用了外函数的参数
    def inner():
        print('我是外函数中的内涵数1')
        f()
        print('我是外函数中的内涵数2')
    return inner


#定义普通函数
def old():
    print('我是一个函数')


if __name__ == '__main__':
    # 原理
    old = outer(old)     #outer返回了inner，赋值给了old
    old()                #此时再调用old函数时，等同于调用了inner函数
'''

def outer(f):
    #定义内涵数,并且在内涵数中调用了外函数的参数
    def inner():
        print('我是外函数中的内涵数1')
        f()
        print('我是外函数中的内涵数2')
    return inner
#改为装饰器用法
@outer            #此处使用@outer的语法就是把outer作为装饰器，等同于old=outer(old)
def old():
    print('我是一个函数')
if __name__ == '__main__':
    old()       #old函数经过outer装饰，代码和调用方法不变，但是函数功能发生了改变