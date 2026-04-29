import csv
from tkinter.font import names

import matplotlib.pyplot as plt

def open_csv():
    with open("test.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)

def open_csv2():
    with open("test.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            print(index, row)

def csv_max():
    with open("test.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[1]) # выводим только имена


# todo КРИВАЯ ДИОГРАММА !
def diagram_from_csv():
    with open("test.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        mp = {}
        for row in reader:
            mp[row[0]] = row[2]

        names = mp.keys()
        arr = mp.values()

        print(names)
        print(arr)

        plt.bar(names, arr)
        plt.show()