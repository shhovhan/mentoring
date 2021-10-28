def buble_sort(arr):
    size = len(arr)
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr


print(buble_sort([5, 2, 66, 34, 23, 45, 37, 77, 36, 3, 7, 82, 19, 24]))
