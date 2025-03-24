import pytest

from src.utils import sort_vacancies


def test_sort_vacancies(vacancy_1, vacancy_2):
    result = sort_vacancies([vacancy_2, vacancy_1], 2)
    assert result == [vacancy_1, vacancy_2]


def test_sort_vacancies_typeerror():
    with pytest.raises(TypeError) as exc_info:
        sort_vacancies([1, 2, 3], 2)
        assert str(exc_info.value) == "Передан неверный тип данных"
