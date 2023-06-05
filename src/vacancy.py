

class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, name: str, url: str, salary_to: int, salary_from: int, description: str):
        self.name = name                    # Профессия
        self.url = url                      # Ссылка на вак.
        self.salary_to = salary_to          # Зарплата
        self.salary_from = salary_from      # Город
        self.description = description      # Опыт работы

    def __str__(self):
        return f'"Специальность: {self.name}", "Ccылка на вакансию: {self.url}",' \
               f' "Зарплата: {self.salary_to}", "Город: {self.salary_from}", "{self.description}"'

    def __eq__(self, other):
        """
        Позволяет реализовать проверку на равенство для экземпляров пользовательских типов.
        :param other: vacancy - экземпляр класса JobParser
        :return: bool
        """
        return self.salary_to == other.salary

    def __lt__(self, other):
        """
        Позволяет реализовать проверку на «меньше чем» для экземпляров пользовательских типов.
        :param other: vacancy - экземпляр класса vacancy
        :return: bool
        """
        return self.salary_to < other.salary