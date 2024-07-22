class Vacancy:
    """
    Класс для работы с вакансиями
    """
    vac_list = []
    def __init__(self,id:int, name: str, city: str, salary_from: int, salary_to: int|None, url: str, requirement: str,responsibility:str):
        self.id = id
        self.name = name
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        Vacancy.vac_list.append(id)

    def __str__(self):
        return (f"{self.name}\n"
                f"Id: {self.id}\n"
                f"Город: {self.city}\n"
                f"Зарплата от: {self.salary_from } \n"
                f"Зарплата до: {self.salary_to if self.salary_to else "Не указана"} \n"
                f"Ссылка: {self.url}\n"
                f"Требования: {self.requirement}\n"
                f"Обязанности: {self.responsibility}\n")




vac1=Vacancy(10,"name1","Город Н",100,None,"https://gg.com","Уметь всё","Жить на работе")
vac2=Vacancy(11,"name2","Город F",105,120,"https://gg.com","Уметь всё","Жить на работе")
vac3=Vacancy(12,"name3","Город V",110,130,"https://gg.com","Уметь всё","Жить на работе")
vac4=Vacancy(13,"name4","Город Z",120,150,"https://gg.com","Уметь всё","Жить на работе")

# print(vac1,vac2,vac3,vac4)
# print(Vacancy.vac_list)



vacancies_list = []
vacancies_list.append(vac1)
vacancies_list.append(vac2)
vacancies_list.append(vac3)
vacancies_list.append(vac4)
sort_by_salary = sorted(vacancies_list, key=lambda x: x.salary_from, reverse=True)
for item in sort_by_salary:
    print(item)