from src.api_connection import HH
from src.utils import sort_vacancies
from src.vacancies import Vacancy
from src.file_handler import JsonFileHandler


def main():
    """
    Функция для взаимодействия с пользователем, соединяющая в себе весь основной функционал
    """
    print('Добро пожаловать! Это программа для поиска необходимых вам вакансий.')
    keyword = input('Введите ключевое слово для поиска: ')
    print('Подождите, идет загрузка вакансий...')
    hh_data = HH()
    data = hh_data.get_vacancies(keyword)
    vacancies = Vacancy.from_hh_data(data)

    top_n = input('Вывести топ-N вакансий с высокой зарплатой? Введите да или нет: ')
    if top_n.lower().strip() == 'да':
        n = int(input('Топ из скольких вакансий вы хотели бы видеть? Введите число: '))
        result = sort_vacancies(vacancies, n)
    else:
        result = vacancies

    saver = JsonFileHandler()
    if not result:
        print("Нет вакансий для записи.")
    else:
        for v in result:
            saver.writer(v)
        print('Вакансии записаны в файл "vacancies.json"')
    pass


if __name__ == '__main__':
    main()
