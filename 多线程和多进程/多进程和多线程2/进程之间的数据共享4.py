


import multiprocessing,time


def task(conn):
    time.sleep(1)
    conn.send([111,22,33,44])
    data = conn.recv()  #阻塞
    print('子进程接受：',data)
    time.sleep(2)


if __name__ == '__main__':
    parent_conn,child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=task,args=(child_conn,))
    p.start()

    info = parent_conn.recv()   #阻塞
    print('主进程接受',info)
    parent_conn.send(666)

