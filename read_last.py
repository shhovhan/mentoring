def read_last(lines_count, file):
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


print(read_last(2, './article.txt'))
