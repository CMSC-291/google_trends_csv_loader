#!/usr/bin/env python
import csv
from datetime import datetime
from sys import argv

from matplotlib import pyplot
from matplotlib.dates import date2num, YearLocator, MonthLocator, DateFormatter


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
            for col_number, data in enumerate(row):
                # for col_number in range(len(row)):
                #     popularity_value = row[col_number]
                if col_number > 0:
                    data_float = float(data)
                    if data_float > max_value:
                        max_value = data_float
                        max_col_number = col_number
        return self.headers[max_col_number]

    def time_most_popular(self, col_number):
        """
        Returns the date that the search term in column col_number was most
        popular
        :param col_number: a column number in the db, between 1 and number of
         terms, inclusive
        :return: a date
        """
        pass

    def plot(self, col_number=1, save_file="test.png"):
        if col_number >= len(self.headers) or col_number < 1:
            raise ValueError("Column number ({}) is out of range.  "
                             "Value numbers are 1 to {}".format(
                col_number,
                len(self.headers) - 1
            ))
        dates = []
        data = []
        for row in self.table:
            dates.append(row[0])
            data.append(float(row[col_number]))
        fig, ax = pyplot.subplots()
        ax.plot(dates, data)

        ax.set(xlabel='date', ylabel='popularity',
               title=self.headers[col_number])
        ax.grid()

        fig.savefig(save_file)
        pyplot.show()

    def plot_all(self, save_file='all.png'):
        dates = []
        lines = []
        for i in range(len(self.headers) - 1):
            lines.append(list())
        for row in self.table:
            dates.append(date2num(datetime.strptime(row[0], '%Y-%m-%d')))
            for col, cell in enumerate(row[1:]):
                lines[col].append(float(cell))
            # data.append(row[col_number])

        fig, ax = pyplot.subplots()
        # for col, line in enumerate(lines):
        #     ax.plot(dates, line, label=self.headers[col])
        for line in lines:
            ax.plot_date(dates, line, '-')

        title = "\nvs\n".join(self.headers[1:])


        ax.set(xlabel='date', ylabel='popularity',
               title=title)
        ax.grid()
        ax.set_ylim([0, 100])

        ax.format_xdata = DateFormatter('%Y-%m-%d')
        ax.grid(True)

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate()

        fig.savefig(save_file)
        pyplot.show()


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage is stats.py [filename]")
    analyzer = GoogleTrendAnalyzer(argv[1])
    print(analyzer.most_popular())
    # analyzer.plot(1)
    analyzer.plot_all()
