# 上下文管理器

class Sample():
    def __enter__(self):
        print("enter")
        # 获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("do something")


def ecx_try():
    try:
        print("code started")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:
        '''
        1.可做资源的释放
        '''
        print("finally")
        return 4


if __name__ == '__main__':
    result = ecx_try()
    print(result)
    with Sample() as sample:
        sample.do_something()
