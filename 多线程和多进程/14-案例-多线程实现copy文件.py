# -*- coding: utf-8 -*-


import time
import threading
import os

def copy_file(file_name,source_dir,dest_dir):
    #拼接源文件路径和目标文件路径
    print  source_dir,file_name
    source_path = source_dir + '\\' + file_name
    print  source_path
    dest_path = dest_dir + '\\' + file_name
    #打开源文件和目标文件，循环读取源文件到目标路径
    with open(source_path,'rb') as source_file:
        with open(dest_path,'wb') as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    source_dir = 'F:\\friends_head_img'
    dest_dir = 'C:\\Users\\zhaoning\Desktop\\test'

    #2.创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print '目标文件夹已存在'
     #3，获取原文件下所有文件
    file_list = os.listdir(source_dir)
    print 111
    print file_list
    #4,遍历文件列表实现copy
    for file_name in file_list:
        print 222
        #5，使用多线程copy
        sub_process = threading.Thread(target=copy_file,args=(file_name,source_dir,dest_dir))
        sub_process.start()
