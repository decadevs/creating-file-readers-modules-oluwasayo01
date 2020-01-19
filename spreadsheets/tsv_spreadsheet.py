from spreadsheets.spreadsheet import Spreadsheet
import pandas as pd

class Tsv(Spreadsheet):

    def __init__(self, filepath):
        self.dataframe = pd.read_csv(filepath, sep="\t")

    def read_first_two_rows(self):
        return super().read_first_two_rows()

    def read_last_two_rows(self):
        return super().read_last_two_rows()

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        return super().__next__()