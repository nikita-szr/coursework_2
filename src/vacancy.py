class Vacancy:
    __slots__ = ("name", "url", "salary", "description", "experience")

    def __init__(self, name: str, url: str, salary: int, description: str, experience: str):
        """Конструктор класса"""
        self.name = name
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.experience = experience

    def __str__(self):
        """ Строковое представление вакансии """
        return (f"Vacancy(title={self.name}, url={self.url}, salary={self.salary}, "
                f"description={self.description}), experince={self.experience}")

    def __lt__(self, other) -> bool:
        """ Метод сравнения зарплаты"""
        return self.salary < other.salary

