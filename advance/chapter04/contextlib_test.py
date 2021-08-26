
import contextlib

@contextlib.contextmanager
#修饰一个生成器
def file_open(file_name):
    print("file open")  #enter
    yield {}
    print("file end") #exit

with file_open("bobby.txt") as  f_opened:
    print("file processimg")