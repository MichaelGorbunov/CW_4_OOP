from src.vacancy import Vacancy
from src.get_data_api import HeadHunterAPI
from src.file_operation import FileOperation
def user_interaction():
    print("Здравствуйте.Это программа выводит информацию о вакансиях,\n"
          "опубликованных на сайте hh.ru")


    print("Начнем с получения списка вакансий по выбранной профессии\n")
    print("Введите название профессии,например - программист\n")
    search_vacancy = input("Введите запрос:\n")
    print(f"Будем искать вакансии по запросу : {search_vacancy}")

    vac_data_list=HeadHunterAPI(search_vacancy).get_vacans_short()

    print(f"Найдено - {len(vac_data_list)} вакансий")

    vac_obj_list = []
    for item in vac_data_list:
        vac_obj_list.append(Vacancy(**item))

    print("Отсортируем по зарплате и выведем топ самых высокооплачиваемых")

    top_n =int(input("Ведите количество вакансий для вывода "))
    sort_vac_obj_list=Vacancy.vacancies_sort_salary()[0:top_n]
    for item in sort_vac_obj_list:
        print(item)

    print("Сохранимся")

    # import json
    #
    # # data - строка, тип str
    # data = '{"name": "John Smith", "age": 30, "city": "New York"}'
    # # parsed_data - словарь, тип dict
    # parsed_data = json.loads(data)
    vac_dict_list=[]
    for item in sort_vac_obj_list:#сериализация в json
        vac_dict_list.append(
            {
                "id": item.id,
                "name": item.name,
                "city": item.city,
                "salary_from": item.salary_from,
                "salary_to": item.salary_to,
                "url": item.url,
                "requirement": item.requirement,
                "responsibility": item.responsibility,
            })

    save=FileOperation(search_vacancy)
    save.write_file(vac_dict_list)




    pass


 # # получение коротки[ данных из api
 #    search_vacancy = input("Введите запрос:\n")
 #    # data1 = HeadHunterAPI.get_vacans_short(HeadHunterAPI(search_vacancy))
 #    data1 = HeadHunterAPI(search_vacancy).get_vacans_short()
 #    # data1 =data11.get_vacans_short()
 #
 #    test_list = []
 #    # print(len(data1))
 #    for item in data1:
 #        test_list.append(item)
 #    #     print(item)
 #    #     print(item["area"]["name"])  # city
 #    print(type(data1))
 #
 #    # data2=JSONData(os.path.join(DATA_DIR, save_file_name+"_"+search_vacancy+".json"))
 #    # data2.write_file(test_list)
 #    with open(
 #        os.path.join(DATA_DIR, save_file_name + "_" + search_vacancy + ".vac"),
 #        "w",
 #        encoding="utf-8",
 #    ) as f:
 #        json.dump(test_list, f, ensure_ascii=False, indent=4)