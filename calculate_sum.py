import tracemalloc


def calculate_sum_with_for(arr):
    """
    Calculate summary of all elements in array using for loop
    :param arr: given array
    :return: summary of all elements in array
    """
    sum_of_numbers = 0
    for i in arr:
        sum_of_numbers += i

    return sum_of_numbers


def calculate_sum_with_while(arr):
    """
    Calculate summary of all elements in array using while loop
    :param arr: given array
    :return: summary of all elements in array
    """
    sum_of_numbers = 0
    i = 0
    while i < len(arr):
        sum_of_numbers += arr[i]
        i += 1

    return sum_of_numbers


def calculate_sum_with_recursion(arr):
    """
    Calculate summary of all elements in array by recursion
    :param arr: given array
    :return: summary of all elements in array
    """
    if len(arr) == 0:
        return 0
    return arr[0] + calculate_sum_with_recursion(arr[1:])


if __name__ == '__main__':
    tracemalloc.start()

    calculate_sum_with_for([1, 2, 3, 4, 5, 6, 7, 8, 9])
    snapshot_1 = tracemalloc.take_snapshot()
    print('SNAPSHOT 1')
    for stat in snapshot_1.statistics('lineno'):
        print(stat)

    calculate_sum_with_while([1, 2, 3, 4, 5, 6, 7, 8, 9])
    snapshot_2 = tracemalloc.take_snapshot()

    calculate_sum_with_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9])
    snapshot_3 = tracemalloc.take_snapshot()
    tracemalloc.stop()
    print('SNAPSHOT 3')
    for stat in snapshot_3.statistics('lineno'):
        print(stat)

    for diff in snapshot_1.compare_to(snapshot_3, 'lineno'):
        print(diff)
