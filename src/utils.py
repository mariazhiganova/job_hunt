from src.vacancies import Vacancy


def sort_vacancies(vacancies: list[Vacancy], n: int) -> list[Vacancy]:
    """
    Функция для сортировки вакансий по зарплате по убыванию и вывода топ-n.
    """
    if all(isinstance(vacancy, Vacancy) for vacancy in vacancies):
        sorted_vacancies = sorted(vacancies, reverse=True)
        return sorted_vacancies[:n]

    else:
        raise TypeError("Передан неверный тип данных")
