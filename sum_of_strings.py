def sum_of_strings(str1, str2):
    """
    Calculate sum of given strings, which contain only integers without using int() function to convert strings
    :param str1: first string of integer numbers
    :param str2: second string of integer numbers
    :return: Sum of converted strings
    """
    int1 = 0
    int2 = 0
    for s1 in str1:
        int1 = int1 * 10 + ord(s1) - 48

    for s2 in str2:
        int2 = int2 * 10 + ord(s2) - 48

    return int2 + int1


if __name__ == '__main__':
    print(sum_of_strings("1223", "45678"))
