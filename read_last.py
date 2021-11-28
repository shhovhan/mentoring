def read_last(lines_count, file):
    """
    Function to return last n lines
    :param lines_count: how many lines to return
    :param file: Filename to read lines
    :return: Last lines_count of lines from file
    """
    if lines_count < 0:
        print('Positive integer must be given as a lines count')
        return

    with open(file, 'r') as f:
        lines = f.readlines()

    if lines_count > len(lines):
        print('There is no enough lines in the file')
        return

    for line in lines[-lines_count:]:
        return line


if __name__ == '__main__':
    print(read_last(2, './article.txt'))
