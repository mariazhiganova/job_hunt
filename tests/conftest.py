import pytest

from src.api_connection import HH
from src.vacancies import Vacancy


@pytest.fixture
def vacancy_1():
    return Vacancy("Разработчик", "https://some_url", 150000, "Знание Python")


@pytest.fixture
def vacancy_2():
    return Vacancy("Бармен", "https://some_url_else", 130000, "Опыт работы от 1 года")


@pytest.fixture
def vacancy_without_salary():
    return Vacancy("Тестировщик", "https://some_url_else_3", None, "Опыт работы от 3 лет")


@pytest.fixture
def dict_vacancies():
    return [
        {
            "name": "Разработчик",
            "alternate_url": "https://some_url",
            "salary": {"from": 150000},
            "snippet": {"requirement": "Знание Python"},
        },
        {
            "name": "Тестировщик",
            "alternate_url": "https://another_url",
            "salary": {"from": 100000},
            "snippet": {"requirement": None},
        },
    ]


@pytest.fixture
def hh():
    return HH()


@pytest.fixture
def mock_open(mocker):
    return mocker.patch("builtins.open", mocker.mock_open(read_data="[]"))


@pytest.fixture
def mock_exists(mocker):
    return mocker.patch("os.path.exists", return_value=False)
