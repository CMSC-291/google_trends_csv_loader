#!/usr/bin/env python
from sys import argv


class GoogleTrendAnalyzer:
    def __init__(self, filename):
        self.filename = filename

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
