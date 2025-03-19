import pytest

from src.vacancies import Vacancy


def test_vacancy_init(vacancy_1):
    assert vacancy_1.name == "Разработчик"
    assert vacancy_1.url == "https://some_url"
    assert vacancy_1.salary == 150000
    assert vacancy_1.requirement == "Знание Python"


def test_vacancy_print(capsys, vacancy_1):
    print(str(vacancy_1))
    captured = capsys.readouterr()

    expected_output = (
        "Вакансия Разработчик:\nСсылка на вакансию: https://some_url\nОклад от 150000\nТребования: Знание Python\n"
    )
    assert captured.out == expected_output


def test_vacancy_comparison(vacancy_1, vacancy_2):
    assert vacancy_1 != vacancy_2

    assert vacancy_1 > vacancy_2
    with pytest.raises(TypeError):
        result = vacancy_1 < "not a Vacancy"


def test_salary_validation(vacancy_without_salary):
    assert vacancy_without_salary.salary == 0


def test_vacancy_to_dict(vacancy_1):
    result = vacancy_1.to_dict()
    assert result == {
        "name": "Разработчик",
        "url": "https://some_url",
        "salary": 150000,
        "requirement": "Знание Python",
    }


def test_from_hh_data(dict_vacancies):
    result = Vacancy.from_hh_data(dict_vacancies)
    assert len(result) == 2
    assert result[0].name == "Разработчик"
    assert result[1].name == "Тестировщик"
