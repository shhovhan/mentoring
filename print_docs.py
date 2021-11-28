from pathlib import Path


def print_docs(directory):
    """
    Print files and subdirectories in given directory
    :param directory: Given direcotory
    :return: Nothing. Prints filenames and directory names
    """
    basedir = Path(directory)
    for item in basedir.iterdir():
        if item.is_dir():
            print(item.name)
            print_docs(item)
        elif item.is_file():
            print(item.name)


if __name__ == '__main__':
    DIRNAME = '/home/shushanik_hovhannesyan/Documents/AWS_Training'
    print_docs(DIRNAME)
