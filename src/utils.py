from src.vacancy import Vacancy


def get_top_n_vacancies(file_saver, n):
    vacancies = file_saver.get_data()
    vacancies_objects = [Vacancy(i['name'], i['alternate_url'], i['salary']['from'], i['snippet']['requirement'],
                                 i['experience']['name']) for i in vacancies if i['salary'] and i['salary']['from']]
    top_vacancies = sorted(vacancies_objects, key=lambda x: x.salary_from, reverse=True)[:n]
    return top_vacancies


def search_vacancies_by_keyword(file_saver, keyword):
    vacancies = file_saver.get_data()
    filtered_vacancies = [i for i in vacancies if keyword.lower() in (i['snippet']['requirement'] or "").lower()]
    return [Vacancy(i['name'], i['alternate_url'], i['salary']['from'] if i['salary'] else None,
                    i['snippet']['requirement'], i['experience']['name']) for i in filtered_vacancies]
