from abc import ABC, abstractmethod
import json


class AbstractFileSaver(ABC):
    """Абстрактный класс с методами для записи в файл"""

    @abstractmethod
    def add_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class FileSaverToJSON(AbstractFileSaver):
    """Класс для получения, работы и удаления вакансий из файла"""
    def __init__(self, filename):
        """Конструктор класса"""
        self.vacancy_data = filename

    def get_data(self):
        """Получение данных из JSON файла"""
        try:
            return json.load(open(self.vacancy_data))
        except FileNotFoundError:
            return []

    def add_data(self, vacancies):
        """Добавление данных в JSON файла"""
        data = self.get_data()
        data.extend(vacancies)

        with open(self.vacancy_data, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_data(self):
        """Удаление данных из JSON файла"""
        with open(self.vacancy_data, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
