from abc import ABC, abstractmethod
class Files(ABC):
    
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def get_first_two_lines(self):
        pass

    @abstractmethod
    def get_last_two_lines(self):
        pass


class ReadBytesFromFile(Files):
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

    def __iter__(self):
        return self.file

    def __next__(self):
            return next(self.file)

    def read_file(self):
        self.file.seek(0)
        for line in self.file:
            print(line.strip('\n'))

    def get_first_two_lines(self):
        self.file.seek(0)
        next(self.file)
        return "{}{}\n".format(next(self.file), next(self.file))

    def get_last_two_lines(self):
        self.file.seek(0)
        res = self.file.readlines()[-2:]
        return "{}{}\n".format(res[-2], res[-1])

file1 = ReadBytesFromFile('solid_principle.txt')
file1.read_file()