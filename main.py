from src.cls_api import HH_API, SuperJobAPI
from src.utils import get_sorted_vacancies, get_top_n_vacancies, get_vacancies_with_description, format_vacancy
from src.json_saver import JsonSaver


def user_interaction():
    print("Добро пожаловать в программу по поиску вакансий!")
    city = input("Введите город для поиска: ")
    print("Выберите платформы для получения вакансий:")
    print("1. hh.ru")
    print("2. SuperJob")
    platforms = []
    selected_platforms = input("Введите номера платформ (через запятую): ")
    for platform in selected_platforms.split(","):
        platform = platform.strip()
        if platform == "1":
            platforms.append("hh.ru")
        elif platform == "2":
            platforms.append("SuperJob")

    writer = JsonSaver("all_vacancies.json")

    for platform in platforms:
        if platform == "hh.ru":
            headhunter = HH_API()
            vacancies = headhunter.get_vacancies
            if vacancies:
                writer.write_vacancies(vacancies)
            else:
                print("Не удалось получить данные о вакансиях с HeadHunter")
        elif platform == "SuperJob":
            superjob = SuperJobAPI()
            vacancies = superjob.get_vacancies(city)
            if vacancies:
                writer.write_vacancies(vacancies)
            else:
                print("Не удалось получить данные о вакансиях с SuperJob")

    print("Данные о вакансиях успешно сохранены!")

    while True:
        print("\nМеню:")
        print("1. Получить топ N вакансий по зарплате")
        print("2. Получить вакансии в отсортированном виде")
        print("3. Получить вакансии с ключевыми словами в описании")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            n = int(input("Введите количество вакансий для вывода в топ N: "))
            top_vacancies = get_top_n_vacancies("all_vacancies.json", n)
            for vacancy in top_vacancies:
                print(format_vacancy(vacancy))
        elif choice == "2":
            sorted_vacancies = get_sorted_vacancies("all_vacancies.json")
            for vacancy in sorted_vacancies:
                print(format_vacancy(vacancy))
        elif choice == "3":
            keywords = input("Введите ключевые слова через запятую: ")
            vacancies_with_description = get_vacancies_with_description("all_vacancies.json", keywords)
            for vacancy in vacancies_with_description:
                print(format_vacancy(vacancy))
        elif choice == '4':
            print("Завершена работа программы")
            break
        else:
            print("Неправильный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    user_interaction()
