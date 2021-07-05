import sys

reload(sys)
sys.setdefaultencoding('utf8')


def Binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) / 2
        print 1111
        print arr[mid]
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find(data, k):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if k == data[mid]:
            return mid
        elif k < data[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1

# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 7, 8]
#     print find(arr,1)

if __name__ == "__main__":
    # 二分查找要求线性表有序
    result = find([49, 38, 65, 97, 76, 13, 27, 49],76)
    print result

