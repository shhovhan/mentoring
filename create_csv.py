import csv
import time

from datetime import datetime


def create_csv():
    """
    Create csv which contains current minutes, seconds and microseconds of PC
    :return: Created CSV file
    """
    with open('rows_300.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['#', 'Minutes', 'Seconds', 'Microseconds'])

        for i in range(1, 301):
            dt = datetime.now()

            writer.writerow([i, dt.minute, dt.second, dt.microsecond])
            time.sleep(2)


if __name__ == '__main__':
    create_csv()
