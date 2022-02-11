import threading
import time


class Foo:
    pass





class Singleton:
    instance = None
    obj_lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:
            return cls.instance

        with cls.obj_lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance


def task():
    obj = Singleton('x')
    print(obj)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task)
        t.start()
