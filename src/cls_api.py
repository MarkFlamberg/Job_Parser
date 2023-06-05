from abc import ABC, abstractmethod
import requests
import os
from src.vacancy import Vacancy


class AbstractApiClass(ABC):
    """ Абстрактный класс для работы с разными API.
        Обязывает создать метод получения вакансии для каждого сайта отдельно
    """

    @abstractmethod
    def get_vacancies(self):
        pass


class HH_API(AbstractApiClass):
    """
    Получаем данные с hh.ru
    """

    @property
    def get_vacancies(self):
        """
        Метод для получения вакансий с сайта HH.ru.
        """

        url = 'https://api.hh.ru/vacancies'
        params = {'area': 1, 'text': 'python',
                  'per_page': 10}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = []
            for item in data['items']:
                salary = item.get('salary', {})
                vacancies.append(
                    Vacancy(
                        name=item['name'],
                        url=item['url'],
                        description=item['snippet']['requirement'],
                        salary_to=salary.get('to') if salary is not None else None,
                        salary_from=salary.get('from') if salary is not None else None
                    )
                )
            return vacancies
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None


class SuperJobAPI(AbstractApiClass):
    """
    Класс SuperJobAPI - класс для получения вакансий с сайта SuperJob.ru."
    """

    def get_vacancies(self, city):
        """
        Метод для получения вакансий с сайта HH.ru.
        Args:
            city (str): Название города, для которого нужно получить вакансии.

        Returns:
            list: Список объектов класса Vacancy.
        """
        api_key: str = os.getenv('SJ_API_KEY')
        api_url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': api_key}
        params = {'keyword': 'python',
                  'town': city}
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            vac = []
            for el in data['objects']:
                try:
                    vac.append(
                        Vacancy(
                            name=el['profession'],
                            url=el['client']['link'],
                            description=el['vacancyRichText'],
                            salary_to=el['payment_to'],
                            salary_from=el['payment_from']
                        )
                    )
                except KeyError:
                    continue
            return vac
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None