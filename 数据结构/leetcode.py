

class Solution(object):

    def bubble_sort(self,arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

    def bubble_sort_advantage(self,arr):
        for i in range(len(arr)-1):
            count = 0
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    count += 1
            if count == 0:
                break
        return arr

    def quick_sort(self,arr,start,end):
        if start < end:
            low,high = start, end
            mid = arr[low]
            while low != high:
                while low < high and arr[high] >= mid:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] < mid:
                    low += 1
                arr[high] = arr[low]
            arr[low] = mid
            self.quick_sort(arr,start,low)
            self.quick_sort(arr,low+1,end)
        return arr

    def insert_sort(self,arr):
        for i in range(1,len(arr)):
            j = i - 1
            temp = arr[i]
            while j >= 0 and temp < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
        return arr

if __name__ == '__main__':
    res1 = Solution().bubble_sort([49,38,65,97,76,13,27,49])
    res2 = Solution().bubble_sort_advantage([49,38,65,97,76,13,27,49])
    res3 = Solution().quick_sort([49,38,65,97,76,13,27,49],0,len([49,38,65,97,76,13,27,49])-1)
    res4 = Solution().insert_sort([49,38,65,97,76,13,27,49])
    print(res1)
    print(res2)
    print(res3)
    print(res4)