# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def insert_sort(nums):
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums


if __name__ == "__main__":
    result = insert_sort([49, 38, 65, 97, 76, 13, 27, 49])
    print result

