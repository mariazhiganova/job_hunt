from abc import ABC, abstractmethod

import requests


class BaseParser(ABC):
    """
    Абстрактный класс, содержащий абстрактный метод, для работы с API сервиса с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def __connection(self):
        pass


class HH(BaseParser):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __connection(self) -> list:
        """
        Метод, который подключается к апи hh.ru и получает вакансии в формате json словарей
        """
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response.json()["items"]

        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
            return []

    def get_vacancies(self, keyword: str) -> list:
        """
        Метод, который фильтрует вакансии по ключевому слову и добавляет их в список
        """
        self.__params["text"] = keyword
        self.__params["page"] = 0
        all_vacancies = []

        while self.__params["page"] < 20:
            items = self.__connection()
            all_vacancies.extend(items)

            self.__params["page"] += 1

        return all_vacancies
