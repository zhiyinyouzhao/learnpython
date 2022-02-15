


from multiprocessing import Process,Array

def f(data_array):
    data_array[0] = 666


if __name__ == '__main__':
    arr = Array('i',[11,22,33,44])
    p = Process(target=f,args=(arr,))
    p.start()
    p.join()
    print(arr[:])
