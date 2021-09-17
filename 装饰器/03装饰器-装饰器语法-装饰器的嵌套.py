

def outer(f):
    def inner():
        print('找到妹子，成功拿到微信...3')
        f()
        print('约妹子，看一场午夜电影...4')
    return inner


def kuozhan(f):
    def kuozhaninner():
        print('扩展1')
        f()
        print('扩展2')
    return kuozhaninner

@kuozhan
@outer
def love():
    print('跟妹子畅谈人生和理想...5')

love = outer(love)     #love = inner
love = kuozhan(love)   #love = kuozhaninner
if __name__ == '__main__':
    love()
    '''
    执行顺序：1,3,5,4,2
    1，先使用离得近的outer装饰器，装饰love函数，返回了一个inner函数
    2.再使用上面的kuozhan装饰器，装饰上一次返回的inner函数，又返回了kuozhaninner函数
    '''