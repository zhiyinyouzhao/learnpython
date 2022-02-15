


from multiprocessing import Process,Value,Array

def func(n,m1,m2):
    n.value = 888
    m1.value = 'a'.encode('utf-8')
    m2.value = '武'


if __name__ == '__main__':
    num = Value('i',666)
    v1 = Value('c')
    v2 = Value('u')

    p = Process(target=func,args=(num,v1,v2))
    p.start()
    p.join()
    print(num.value) #888
    print(v1.value) #a
    print(v2.value) #武

