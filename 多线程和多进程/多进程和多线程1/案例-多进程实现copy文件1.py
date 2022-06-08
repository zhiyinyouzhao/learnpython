
import os
import multiprocessing
'''
    需求：
        1.目标文件是否存在，如果不存在就创建，如果存在则不创建
        2.遍历源文件夹中所有文件，并拷贝到目标文件夹
        3.采用进程实现多任务，完成高并发拷贝

'''

def copy_file(file_name,source_dir,dest_dir):
    source_file = "%s%s%s" %(source_dir,'\\',file_name)
    dest_file = "%s%s%s" %(dest_dir,'\\',file_name)
    print('copy_file进程的pid:', os.getpid())
    print('copy_file进程的父进程pid:', os.getppid())
    print("源文件：%s,目标文件：%s" %(source_file,dest_file))
    with open(source_file,'rb') as src:
        with open(dest_file,'wb') as dst:
            while True:
                data = src.read(1024)
                if data:
                    dst.write(data)
                else:
                    break


def copy():
    print('copy进程的pid:', os.getpid())
    source_dir = 'F:\\friends_head_img'
    dest_dir = 'C:\\Users\\zhaoning\Desktop\\test'
    try:
        os.mkdir(dest_dir)
    except Exception as e:
        print('目标文件已存在：%s' %e)
    file_list = os.listdir(source_dir)
    for file_name in file_list:
        sub_process = multiprocessing.Process(target=copy_file,kwargs={'file_name':file_name,'source_dir':source_dir,'dest_dir':dest_dir})
        sub_process.start()

if __name__ == '__main__':
    print('主进程的pid:', os.getpid())
    copy()


