STRING1 = "1223"
STRING2 = "45678"


def sum_of_strings(str1, str2):
    int1 = 0
    int2 = 0
    for s1 in str1:
        int1 = int1 * 10 + ord(s1) - 48

    for s2 in str2:
        int2 = int2 * 10 + ord(s2) - 48

    return int2 + int1


print(sum_of_strings(STRING1, STRING2))
