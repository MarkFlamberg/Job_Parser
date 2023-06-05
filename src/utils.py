import json


def get_top_n_vacancies(filename: str, n: int):
    """Сортирует вакансии по значению зарплаты от наивысшей до наименьшей"""
    with open(filename, 'r', encoding='utf-8') as file:
        vacancies = json.load(file)

    sorted_vacancies = sorted(vacancies, key=lambda x: x.get('salary_from', 0) or 0, reverse=True)
    filtered_vacancies = [v for v in sorted_vacancies if v.get('salary_from') is not None and v.get('salary_from') > 0]

    return filtered_vacancies[:n]


def get_sorted_vacancies(filename: str):
    """Сортирует вакансии по имени (алфавитный порядок)"""
    with open(filename, 'r', encoding='utf-8') as file:
        vacancies = json.load(file)

    sorted_vacancies = sorted(vacancies, key=lambda x: x['name'])
    return sorted_vacancies


def get_vacancies_with_description(filename: str, keywords: list):
    """Фильтрует вакансии, оставляя только те, у которых описание (description)"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    filtered_vacancies = []
    for vacancy in data:
        description = vacancy.get('description')
        if description:
            description = description.lower()
            for keyword in keywords:
                if keyword.lower() in description:
                    filtered_vacancies.append(vacancy)
                    break
    return filtered_vacancies

def format_vacancy(vacancy: dict):
    """Форматирует информацию о вакансии в виде строки с указанием названия, ссылки, зарплаты (от и до), и описания."""
    return f"Название: {vacancy['name']}\n" \
           f"Ссылка: {vacancy['url']}\n" \
           f"Зарплата от: {vacancy['salary_from']}\n" \
           f"Зарплата до: {vacancy['salary_to']}\n" \
           f"Описание: {vacancy['description']}\n"
