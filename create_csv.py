import csv
import time

from datetime import datetime

file_name = 'rows_300.csv'


def create_csv(file):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['#', 'Minutes', 'Seconds', 'Microseconds'])

        for i in range(1, 301):
            dt = datetime.now()

            writer.writerow([i, dt.minute, dt.second, dt.microsecond])
            time.sleep(2)


create_csv(file_name)
