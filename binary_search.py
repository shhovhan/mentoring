def binary_search(arr, l, r, x):
    if r > l:
        mid = (r + l)//2
        if arr[mid] == x:
            return x

        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(ARRAY, 0, len(ARRAY), 2))
