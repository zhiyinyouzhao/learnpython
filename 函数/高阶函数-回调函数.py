


def func(f):
    print(f,type(f))
    f()



#回调函数
def love():
    print('123')

if __name__ == '__main__':
    func(love)