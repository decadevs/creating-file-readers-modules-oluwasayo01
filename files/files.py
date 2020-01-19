from abc import ABC, abstractmethod


class File(ABC):
    
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
    def read_first_two_lines(self):
        pass

    @abstractmethod
    def read_last_two_lines(self):
        pass


