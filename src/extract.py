import pandas as pd
import csv
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, 'CSV', 'test.csv')

data = pd.read_csv(csv_path, usecols=[0])
test = data.values.tolist()


def roll_curator():
    """[extracts the rolls from CSV and appends to list]
    
    Returns:
        [list] -- [contains first four digits of the first column]
    """

    roll_list = ['START']

    for line in test:
        for item in line:
            if item[:4] == roll_list[-1]:
                continue
            else:
                roll_list.append(item[:4])

    return roll_list

rolls = roll_curator()
