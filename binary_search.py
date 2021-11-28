def binary_search(arr, l, r, x):
    """
    Recursive implementation of binary search algorithm
    :param arr: given array, where element should be founded or not
    :param l: left index from where start search
    :param r: right index where to stop search
    :param x: element that should be found in arr
    :return: return index of element if it exists, otherwise -1
    """
    if r > l:
        mid = (r + l)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


if __name__ == '__main__':
    ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(ARRAY, 0, len(ARRAY), 2))
