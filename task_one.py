"""
To get details of employees woh's salary is > 9000.
"""

from My_Utils.csv import HandleCSV
from My_Utils.preety_printer import task_one_format


def do_task_one():
    print("Employees who's salary is >9000")
    for emp in HandleCSV.read_csv_line_by_line():
        if int(emp["SALARY"]) > 9000:
         # if salary is >9000, print dictionary with only
         # name, email and phone number
            print(task_one_format(emp))
