def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr


if __name__ == "__main__":
    result = bubble_sort([49, 38, 65, 97, 76, 13, 27, 49])
    print(result)
