

class Outer():

    #魔术方法：该方法把该类对象当作函数调用时，自动触发obj()
    def __call__(self, func):
        print("触发了__call__方法",func)
        self.func = func   #把传进来的函数作为对象的成员方法
        return self.inner   #返回一个函数


    def inner(self,who):
        print('拿到妹子的微信')
        self.func(who)
        print('看一场午夜电影')



#@Outer()            #outer() ==> obj @obj ==>obj(love) ==> __call__(love) ==> inner()
def love(who):
    print(f'{who}和妹子谈谈人生和理想...')




if __name__ == '__main__':
    #love('张三')
    obj = Outer()
    love = obj(love)
    love('思思')
