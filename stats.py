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
        Return the string of the column for the item with highest popularity
        :return:
        """
        pass


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage is stats.py [filename]")
    analyzer = GoogleTrendAnalyzer(argv[1])
    print(analyzer.most_popular())
