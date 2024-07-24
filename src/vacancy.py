from builtins import list


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    vac_list: list = []

    def __init__(
            self,
            id: int,
            name: str,
            city: str,
            salary_from: int,
            salary_to: int,
            url: str,
            requirement: str,
            responsibility: str,
    ):
        self.id = id
        self.name = name
        self.city = city
        self.salary_from = (
            salary_from if salary_from is not None else 0
        )  # None заменяем на 0
        self.salary_to = salary_to if salary_to is not None else 0  # None заменяем на 0
        # self.salary_from = salary_from
        # self.salary_to = salary_to
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        Vacancy.vac_list.append(self)

    def __str__(self):
        return (
            f"{self.name}\n"
            f"Id: {self.id}\n"
            f"Город: {self.city}\n"
            f"Зарплата от: {self.salary_from if self.salary_from else "Не указана"} \n"
            f"Зарплата до: {self.salary_to if self.salary_to else "Не указана"} \n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
            f"Обязанности: {self.responsibility}\n"
        )

    @classmethod
    def vacancies_sort_salary(cls) -> list:
        """
        Сортирует вакансии по зарплате и возвращает отфильтрованный список экземпляров класса по убиванию зарплаты.
        """

        # cls.vac_list.sort(cls.vac_list, key=lambda x: x.salary_from, reverse=True)
        # key=lambda book: book.pages, reverse=True
        cls.vac_list.sort(key=lambda x: x.salary_from, reverse=True)
        return cls.vac_list

    @classmethod
    def vacancies_filtered_city(cls, city) -> list:
        """
        Сортирует вакансии по городу и возвращает список вакансий с нужным городом.
        """
        filter_city: list = []
        for item in cls.vac_list:
            if item.city == city:
                filter_city.append(item)
        return filter_city

    @classmethod
    def filter_vacancies(cls, vacancies_list: list, filter_words: list) -> list:
        """Фильтрация вакансий по ключевым словам"""
        filtered_list = []
        for vacancy in vacancies_list:
            for word in filter_words:
                if word.lower() in vacancy.requirement.lower().split():
                    filtered_list.append(vacancy)

        if len(filtered_list) == 0:
            print(*filter_words)
            print("Вакансий с такими критериями не найден")
        return filtered_list

    def range_from_salary(self, salary_from, salary_to) -> bool:
        """Метод проверки объекта-вакансии перекрытия зарплатной вилки
        salary_from:int зарплата от
        salary_to:int зарплата до
        возвращает bool
        """
        if isinstance(salary_from, int) is True and isinstance(salary_to, int) is True:
            if self.salary_from >= salary_from and self.salary_to >= salary_to:
                return True
            else:
                return False
                # return self


def func1():
    vac1 = Vacancy(
        10, "name1", "Город Н", 100, None, "https://gg.com", "Уметь всё ", "Жить на работе"
    )
    vac2 = Vacancy(
        11, "name2", "Город F", None, 120, "https://gg.com", "Знать всё", "Жить на работе"
    )
    vac3 = Vacancy(
        12, "name3", "Город V", 110, 130, "https://gg.com", "Рулить всем", "Жить на работе"
    )
    vac4 = Vacancy(
        13,
        "name4",
        "Город Z",
        120,
        150,
        "https://gg.com",
        "Ездить на всём",
        "Жить на работе",
    )


def func2():
    filter_words = ["уметь", "знать"]
    # filter_words=["супермен,мегамозг"]

    print("**********************************************")
    vac_list = Vacancy.vac_list
    filtered_vac = Vacancy.filter_vacancies(vac_list, filter_words)
    for item in filtered_vac:
        print(item)


func1()


# func2()

def func3():
    vac_list = Vacancy.vac_list
    sort_list = []
    for item in vac_list:
        if Vacancy.range_from_salary(item, 0, 0) is True:
            sort_list.append(item)
            print(item)
    print(sort_list)
    # print(Vacancy.vac_list)
    # print(Vacancy.vac_list[1].salary_to)


func3()

# # print(vac1,vac2,vac3,vac4)
# Vacancy.vacancies_sort_salary()
# for item in Vacancy.vac_list:
#     print(item)
# print("**********************************************")
# list = Vacancy.vacancies_filtered_city("Город Z")
# for item in list:
#     print(item)


#
# vacancies_list = []
# vacancies_list.append(vac1)
# vacancies_list.append(vac2)
# vacancies_list.append(vac3)
# vacancies_list.append(vac4)
# sort_by_salary = sorted(vacancies_list, key=lambda x: x.salary_from, reverse=True)#сортировка по зарплате
# sort_by_salary = sorted(Vacancy.vac_list, key=lambda x: x.salary_from, reverse=True)#сортировка по зарплате
# for item in sort_by_salary:
#     print(item)


# def filter_vacancies(vacancies_list: list, filter_words: list):
#     """Фильтрация вакансий по ключевым словам"""
#     filtered_list = []
#     for vacancy in vacancies_list:
#         # print(vacancy.requirement.lower().split())
#         for word in filter_words:
#             if word.lower() in vacancy.requirement.lower().split():
#                 filtered_list.append(vacancy)
#
#     if len(filtered_list) == 0:
#         print(*filter_words)
#         print("Вакансий с такими критериями не найден")
#     return filtered_list
