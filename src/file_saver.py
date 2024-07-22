from abc import ABC, abstractmethod


class AbstractFileSaver(ABC):
    """Абстрактный класс с методами для записи в файл"""

    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass
