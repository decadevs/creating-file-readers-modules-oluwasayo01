from abc import ABC, abstractmethod
import pandas as pd

class Spreadsheet(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read_first_two_rows(self):
        return self.dataframe.head(2)

    @abstractmethod
    def read_last_two_rows(self):
        return self.dataframe.tail(2)

    @abstractmethod
    def __iter__(self):
        return self.dataframe

    @abstractmethod
    def __next__(self):
        self.index += 1
        return self.dataframe.iloc[self.index:self.index+1]