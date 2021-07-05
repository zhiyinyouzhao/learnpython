


def quick_sort(arr, low, high):
    if low < high:
        i = low
        j = high
        temp = arr[i]
        while i != j:
            while i < j and arr[j] >= temp:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= temp:
                i += 1
            arr[j] = arr[i]
        arr[i] = temp
        quick_sort(arr, low, i - 1)
        quick_sort(arr, i + 1, high)
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    result = quick_sort([49, 38, 65, 97, 76, 13, 27, 49], 0, 7)
    print(result)
