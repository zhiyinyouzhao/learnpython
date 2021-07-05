# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def shell_sort(arr):
    # 增长量初始值
    h = 1
    while h < len(arr)/2:
        h = 2 * h + 1
    # h 减小规则
    h = h / 2
    while( h> 0):
        #排序
        #待插入元素
        for i in range(h,len(arr)):
            #待插入和有序元素比较
            j = i-h
            temp = arr[i]
            while j >= 0 and temp < arr[j]:
                arr[j+h] = arr[j]
                j -= h
            arr[j+h] = temp
        h = h / 2
    return arr


    



if __name__ == "__main__":
    result = shell_sort([49, 38, 65, 97, 76, 13, 27, 49])
    print result

