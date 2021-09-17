

def outer(f):
    def inner(who,name,*args,**kwargs):
        print('约到妹子，聊微信...')
        f(who,name,*args,**kwargs)
        print('天色已晚，怎么办？')
    return inner



@outer
def love(who,name,*args,**kwargs):
    print(f'{who}跟{name}畅谈人生和理想...')
    print('完事了吃了很多美食',args)
    print('看了一场电影',kwargs)

if __name__ == '__main__':
    love('三多','思思','火锅','7块钱的麻辣烫',mov='唐山大地震')