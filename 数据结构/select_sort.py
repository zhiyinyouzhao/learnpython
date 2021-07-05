import sys

reload(sys)
sys.setdefaultencoding('utf8')


def select_sort(arr):
    for i in range(len(arr)):
        min = i
        j = i+1
        while j < len(arr):
            print j
            if arr[j] < arr[min]:
                min = j
            j += 1
        swap(arr,min,i)
    return  arr


def select_sort(nums):
    for i in range(len(nums)-1):
        # 寻找[i,n]区间里的最小值
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    result = select_sort([49, 38, 65, 97, 76, 13, 27, 49])
    print result
