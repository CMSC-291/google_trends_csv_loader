#!/usr/bin/env python
import csv
from sys import argv


class GoogleTrendAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.table = []
        self.headers = []
        with open(filename, 'r') as f:
            self.title = f.readline().strip()  # get the title of the csv
            f.readline()  # ignore the blank line in the csv
            reader = csv.reader(f)  # get a csv reader from the file handle
            self.headers = reader.__next__()  # read one line which
            # contains the column headers
            for row in reader:
                self.table.append(row)  # add each csv row to my table

    def most_popular(self):
        """
        Return the header of the column for the item with highest popularity
        :return:
        """
        max_col_number = -1
        max_value = float("-inf")
        for row in self.table:
            # for col_number, data in enumerate(row):
            for col_number in range(row):
                data = row[col_number]
                if col_number > 0:
                    data_float = float(data)
                    if data_float > max_value:
                        max_value = data_float
                        max_col_number = col_number
        return self.headers[max_col_number]


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage is stats.py [filename]")
    analyzer = GoogleTrendAnalyzer(argv[1])
    print(analyzer.most_popular())
