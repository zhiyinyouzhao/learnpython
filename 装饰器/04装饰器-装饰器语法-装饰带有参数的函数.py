


def outer(f):
    #如果装饰带有参数的函数，需要在内涵数中定义形参，并且传递给调用的函数，因为调用原函数等于调用内涵数
    def inner(var):
        print('找到妹子，成功拿到微信...')
        f(var)
        print('约妹子，看一场午夜电影...')
    return inner


#有参数的函数
@outer
def love(name):
    print(f'跟{name}妹子畅谈人生和理想...')

if __name__ == '__main__':
    love('思思')