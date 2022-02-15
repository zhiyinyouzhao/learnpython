
import multiprocessing


def task():
    print(name)
    file_object.write("alex\n")
    file_object.flush()



if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []
    file_object = open('x1.txt',mode='a+',encoding='utf-8')
    file_object.write("吴佩琪\n")
    file_object.flush()

    p1 = multiprocessing.Process(target=task)
    p1.start()

    '''
        txt输出：
        吴佩琪
        alex
    '''