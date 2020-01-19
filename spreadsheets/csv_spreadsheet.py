from spreadsheet import Spreadsheet
import pandas as pd

class Csv(Spreadsheet):

    def __init__(self, filepath):
        self.index = 0
        self.dataframe = pd.read_csv(filepath)

    def read_first_two_rows(self):
        return super().read_first_two_rows()

    def read_last_two_rows(self):
        return super().read_last_two_rows()

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        return super().__next__()


x = Csv(r'../spreadsheets/iris.csv')

print(x.read_first_two_rows())
# print(x.read_last_two_rows())

# x = pd.read_csv(r'../spreadsheets/iris.csv')

# for index, row in x.iterrows():
#     print(row['petal.width'], row['petal.length'])
