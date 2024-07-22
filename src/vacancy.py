class Vacancy:
    __slots__ = ("name", "url", "salary_from", "description", "experience")

    def __init__(self, name: str, url: str, salary_from: int, description: str, experience: str):
        """Конструктор класса"""
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from else "Зарплата не указана"
        self.description = description
        self.experience = experience

    def __str__(self):
        """ Строковое представление вакансии """
        return (f"Vacancy(title={self.name}, url={self.url}, salary={self.salary_from}, "
                f"description={self.description}), experince={self.experience}")

    def __repr__(self):
        """ Строковое представление вакансии для отладки"""
        return self.__str__()

    def __eq__(self, other):
        """Сравнивает две вакансии по зарплате на равенство"""
        if type(self) is not type(other):
            raise TypeError("Невозможно сравить объекты разных классов")
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        """Сравнивает две вакансии по зарплате (меньше)"""
        if type(self) is not type(other):
            raise TypeError("Невозможно сравить объекты разных классов")
        return self.salary_from < other.salary_from

    def __le__(self, other):
        """Сравнивает две вакансии по зарплате (меньше или равно)"""
        if type(self) is not type(other):
            raise TypeError("Невозможно сравить объекты разных классов")
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        """Сравнивает две вакансии по зарплате (больше)"""
        if type(self) is not type(other):
            raise TypeError("Невозможно сравить объекты разных классов")
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        """Сравнивает две вакансии по зарплате (больше или равно)"""
        if type(self) is not type(other):
            raise TypeError("Невозможно сравить объекты разных классов")
        return self.salary_from >= other.salary_from
