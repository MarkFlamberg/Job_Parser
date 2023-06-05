import json
from abc import ABC, abstractmethod


class AbstractFilemanager(ABC):
    """
    Абстрактный базовый класс, определяет интерфейс для управления файлами с вакансиями
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancies(self, criteria):
        pass


class Filemanager(AbstractFilemanager):

    def __init__(self, filename: str):
        """Конкретная реализация класса vacancyfilemanager для работы с json-файлами."""
        self.filename = filename

    def add_vacancy(self, vacancy):
        """Открывает файл и добавляет новую вакансию в JSON-формате на отдельной строке"""
        with open(self.filename, 'a', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False)
            file.write('\n')

    def get_vacancies(self, criteria):
        """Считывает содержимое файла, парсит каждую строку вакансии из JSON-формата"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            vacancies = []
            for line in file:
                vacancy = json.loads(line)
                if self.matches_criteria(vacancy, criteria):
                    vacancies.append(vacancy)
            return vacancies

    def delete_vacancies(self, criteria):
        """Считывает содержимое файла, удаляет вакансии из файла"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(self.filename, 'w', encoding='utf-8') as file:
            for line in lines:
                vacancy = json.loads(line)
                if not self.matches_criteria(vacancy, criteria):
                    file.write(line)

    @staticmethod
    def get_top_n_vacancies(filename: str, n: int):
        """Читает содержимое файла, парсит его в список вакансий и возвращает топ N вакансий с наивысшей зарплатой"""
        with open(filename, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)

        sorted_vacancies = sorted(vacancies, key=lambda x: x['salary_from'], reverse=True)
        return sorted_vacancies[:n]

    @staticmethod
    def matches_criteria(vacancy, criteria):
        """Проверяет, соответствует ли вакансия заданным критериям"""
        keywords = criteria.get('keywords', [])
        for keyword in keywords:
            if keyword.lower() in vacancy['description'].lower():
                return True
        return False
