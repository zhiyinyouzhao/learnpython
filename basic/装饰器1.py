
import time

def count_time_wrapper(func):
    '''
    闭包本质上是一个函数，闭包函数的传入参数和返回值也是函数
    闭包函数的返回值是对传入函数进行增强后的结果
    '''

    def improved_func(*args,**kwargs):      # 增强函数应该把接收到的所以参数传给原函数

        print(args)
        print(kwargs)
        start_time = time.perf_counter()    # 起始时间
        ret = func(*args,**kwargs)                              # 执行函数
        end_time = time.perf_counter()      # 结束时间
        print('it takes {} s to find the olds'.format(end_time - start_time))
        return ret                      #增强函数的返回值是原函数的返回值
    return improved_func


def count_odds(lim=100):
    print(lim)
    cnt = 0
    for i in range(lim):
        if i %2 ==1:
            cnt += 1
    return cnt


# 对有含有返回值的函数，调用闭包增强后，不能成功返回，但是成功增强了辅助功能
# 对于含有参数的函数，调用闭包增强后，不能成功接受参数
if __name__ == '__main__':
    print('增强前')
    print(count_odds(lim = 1000000))     #装饰前函数能正常返回，能接受参数
    print('---------------------------')
    print('增强后')
    count_odds = count_time_wrapper(count_odds)
    print(count_odds(lim = 1000000))  # 装饰后函数能正常返回
