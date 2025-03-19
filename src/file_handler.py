import json
import os.path
from abc import ABC, abstractmethod

from settings import JSON_PATH
from src.vacancies import Vacancy


class BaseFileHandler(ABC):
    """
    Абстрактный класс для работы с файлами на чтение и запись
    """

    @abstractmethod
    def reader(self):
        pass

    @abstractmethod
    def writer(self, vacancy):
        pass

    @abstractmethod
    def delete(self, url_to_del):
        pass


class JsonFileHandler(BaseFileHandler):
    """
    Дочерний класс для работы с json файлами
    """

    def __init__(self, file_path=JSON_PATH):
        self.__file_path = file_path
        if not os.path.exists(self.__file_path):
            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def reader(self) -> dict:
        """
        Метод для чтения файлов json
        """
        with open(self.__file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def writer(self, vacancy: Vacancy) -> None:
        """
        Метод для записи json данных (одной вакансии) в файл
        """
        try:
            old_vacancies = self.reader()
            vac_dict = vacancy.to_dict()
            if vac_dict in old_vacancies:
                return

            old_vacancies.append(vac_dict)

            with open(self.__file_path, "w", encoding="utf-8") as f:

                json.dump(old_vacancies, f, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"Ошибка записи в файл: {e}")

    def delete(self, url_to_del: str) -> None:
        """
        Метод для удаления данных из файла
        """
        old_vacancies = self.reader()

        new_data = [vac for vac in old_vacancies if vac["url"] != url_to_del]

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
