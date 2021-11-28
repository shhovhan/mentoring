def reverse_array(arr):
    """
    Function to reverse given array in place
    :param arr: array to reverse
    :return: reversed array of given one
    """
    i = 0
    while i < len(arr)/2:
        arr[i], arr[-i-1] = arr[-i-1], arr[i]
        i = i + 1

    return arr


if __name__ == '__main':
    ARR = [1, 2, 3, 5, 6, 8, 9, 10, 11]
    print(reverse_array(ARR))
