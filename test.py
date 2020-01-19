import unittest

class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.txt = Text(r'../solid_priciple.txt')
        self.csv = CsvFile(r'../iris.csv')
        self.csv_spreadsheet = Csv(r'../iris.csv')

    