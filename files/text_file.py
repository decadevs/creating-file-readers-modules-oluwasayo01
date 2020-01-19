from files import File

class Text(File):
    def __init__(self, filename):
        self.file = filename

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __iter__(self):
        self.fp = open(self.file)
        return self

    def __next__(self):
        return next(self.fp)
        

    def read_file(self):
        with open(self.file) as f:
            for line in f:
                print(line.strip('\n'))

    def read_first_two_lines(self):
        with open(self.file) as f:
            return "{}{}\n".format(next(f), next(f))

    def read_last_two_lines(self):
        with open(self.file) as f:
            last_two = f.readlines()[-2:]
            return "{}{}\n".format(last_two[-2], last_two[-1])
