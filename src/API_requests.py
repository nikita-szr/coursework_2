from abc import ABC, abstractmethod
import requests


class ApiVacancies(ABC):
    """Абстрактный класс для работы api"""
    @abstractmethod
    def get_vacancies(self, search_query: str, page: int = 0) -> list:
        pass


class VacanciesHH(ApiVacancies):
    """Класс для api запроса вакансий с HeadHunter"""
    def __init__(self):
        self.base_url = 'https://api.hh.ru/vacancies'
        self.headers = {
            'User-Agent': "Myscript"
        }

    def get_vacancies(self, search_query: str, page: int = 0) -> list:
        params = {
            'text': search_query,
            'page': page,
            'per_page': 20,
            'area': 113,
        }
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            data = response.json()
            if response.status_code == 200:
                print("Запрос успешно выполнен")
                return data
        except requests.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return []


# vacancies = VacanciesHH()
# result = vacancies.get_vacancies('Python разработчик')
# print(result)