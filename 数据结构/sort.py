
# 1.交换类排序
"""
冒泡排序
            最好      平均      最坏
时间复杂度    O(N)      O(N*N)   O(N*N)
空间复杂度    O(1)
稳定性       稳定
"""
"""
for i in range(len(arr-1),0,-1)
代表[n-1,n-2,...1]
"""
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

"""改进"""
# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         count = 0
#         for j in range(len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 count += 1
#         if count == 0:
#             break
#     return arr


"""
快速排序
            最好              平均          最坏
时间复杂度    O(N*log2N)      O(N*log2N)    O(N*N)
空间复杂度    O(log2n)~O(n) 
稳定性       不稳定
"""
def quick_sort(arr,start,end):
    if start < end:
        low,high = start,end
        mid = arr[low]
        while low != high:
            # 相等的放一边，符合排序稳定
            while low < high and arr[high] >= mid:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < mid:
                low += 1
            arr[high] = arr[low]
        arr[low] = mid
        quick_sort(arr,start,low-1)
        quick_sort(arr,low+1,end)
    return arr


# 2.插入类排序
"""
直接插入排序
"""
def insert_sort(arr):
    for i in range(1,len(arr)):
        temp,j = arr[i],i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

# 3.选择类排序
def select_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr 


if __name__ == '__main__':
    # result1 = bubble_sort([49, 38, 65, 97, 76, 13, 27, 49])
    # print(result1)
    # result2 = quick_sort([49, 38, 65, 97, 76, 13, 27, 49],0,7)
    # print(result2)
    # result3 = insert_sort([49, 38, 65, 97, 76, 13, 27, 49])
    # print(result3)
    result4 = select_sort([49, 38, 65, 97, 76, 13, 27, 49])
    print(result4)







