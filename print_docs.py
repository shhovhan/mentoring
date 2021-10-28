from pathlib import Path
DIRNAME = '/home/shushanik_hovhannesyan/Documents/AWS_Training'


def print_docs(directory):
    basedir = Path(directory)
    for item in basedir.iterdir():
        if item.is_dir():
            print(item.name)
            print_docs(item)
        elif item.is_file():
            print(item.name)


print_docs(DIRNAME)
