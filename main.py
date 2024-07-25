from src.API_requests import ApiVacancies, VacanciesHH
from src.file_saver import AbstractFileSaver, FileSaverToJSON
from src.utils import get_top_n_vacancies, search_vacancies_by_keyword


def main():
    """Запускает программу для работы с пользователем"""
    hh_api = VacanciesHH()
    file_saver = FileSaverToJSON(r"./data/vacancies.json")

    while True:
        print(''''1. Поиск вакансий на hh.ru'
'2. Вывести топ N вакансий по зарплате'
'3. Поиск вакансий по ключевому слову в описании'
'4. Завершить программу''')

        user_choice = input('Введите число: ')
        if user_choice == '1':
            search_query = input("Введите вакансию: ")
            vacancies = hh_api.get_vacancies(search_query)
            file_saver.add_data(vacancies)
            print(f"Найдено {len(vacancies)} вакансий и сохранено в файл 'vacancies.json.'")

        elif user_choice == "2":
            n = int(input("Введите количество вакансий для отображения: "))
            top_vacancies = get_top_n_vacancies(file_saver, n)
            for vacancy in top_vacancies:
                print(vacancy)

        elif user_choice == '3':
            keyword = input("Введите слово для поиска в описании вакансии: ")
            filtered_vacancies = search_vacancies_by_keyword(file_saver, keyword)
            for vacancy in filtered_vacancies:
                print(vacancy)

        elif user_choice == '4':
            print("Программа завершена.")
            break

        else:
            print("Вы ввели то что программа не поняла, извините)")


if __name__ == "__main__":
    main()
