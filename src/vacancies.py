class Vacancy:
    """
    Класс для создания вакансий, имеющих название, ссылку, зп и требования
    """

    __slots__ = ("name", "url", "salary", "requirement")

    def __init__(self, name, url, salary, requirement):
        self.name = name
        self.url = url
        self.salary = self.__salary_validation(salary)
        self.requirement = requirement

    def __str__(self):
        return f"Вакансия {self.name}:\nСсылка на вакансию: {self.url}\nОклад от {self.salary}\nТребования: {self.requirement}"

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return NotImplemented

    def __salary_validation(self, salary):
        """
        Метод для валидации по зарплате: указана ли?
        """
        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary

    def to_dict(self):
        """
        Метод для преобразования экземпляра класса в словарь
        """
        return {"name": self.name, "url": self.url, "salary": self.salary, "requirement": self.requirement}

    @classmethod
    def from_hh_data(cls, vacancies_info):
        """
        Класс-метод для создания списка экземпляров класса
        """
        vacancies = []
        for vac_info in vacancies_info:
            name = vac_info["name"]
            url = vac_info["alternate_url"]
            salary_from = vac_info["salary"]["from"] if vac_info["salary"] else None
            requirement = vac_info["snippet"]["requirement"] if vac_info["snippet"]["requirement"] else "Не указано"

            vacancies.append(cls(name, url, salary_from, requirement))

        return vacancies
