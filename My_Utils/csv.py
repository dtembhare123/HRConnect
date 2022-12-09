import csv
# from pprint import pprint
from csv import DictReader
from typing import Dict


class HandleCSV:
    """
    To read data from csv file.
    class attribute:
        filename

    class methods:
        1. read_entire_csv()
        2. read_csv_line_by_line()
    """
    # filename = "D:\HRConnect-master\employees.csv"
    filename = "C:/Users/DELL/PycharmProjects/HRConnect_Project/employee.csv"
    # absolute path of the csv file

    @classmethod
    def read_entire_csv(cls) -> csv.DictReader:
        """
        Class method to read csv file in Dictionary format
        :return: <csv.DictReader object>
        """
        all_details = []
        with open(cls.filename, "r") as foo:
            dr_object = DictReader(foo)  # Converting file object into
            # DictReader object
            for i in dr_object:
                all_details.append(i)
        return all_details

    @classmethod
    def read_csv_line_by_line(cls) -> Dict:
        """

        Function based generator.
        Class method to read data from csv file line by line in Dictionary format
        :return: csv file's row in Dictionary format
        """
        with open(cls.filename) as bar:
            for line in DictReader(bar):
                yield line

# pprint(HandleCSV.read_entire_csv())
