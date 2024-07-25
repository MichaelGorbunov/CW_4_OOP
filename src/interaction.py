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

    # print("Сохранимся")
    #
    #
    # vac_dict_list=[]
    # for item in sort_vac_obj_list:#сериализация в json
    #     vac_dict_list.append(Vacancy.vac_obj_to_dict(item))
    #
    #
    # save=FileOperation(search_vacancy)
    # save.write_file(vac_dict_list)

    print("Отфильтруем вакансии по зарплатной вилке")
    print("Ведите через запятую желаемый уровень зарплаты,")
    print("от минимально приемлимого до желаемого,")
    print("например 50000,70000")
    print("если указать 0 в качестве одной из границ в диапазон попадут зарплаты," )
    print("в которых граница не задана")

    in_salary_from, in_salary_to = map(int, input("Введите диапазон через запятую : ").split(","))

    for item in sort_vac_obj_list:
        if Vacancy.range_from_salary(item,in_salary_from,in_salary_to) is False:
            sort_vac_obj_list.remove(item)
    print(f"осталось - {len(sort_vac_obj_list)} вакансий  ")
    # for item in sort_vac_obj_list:
    #     print(item)

    print("Отфильтруем по ключевым словам")
    print("Введите через запятую ключевые слова,")
    print("например - без опыта,обучение")

    keyword_list=input("Введите ключевые слова : ").split(",")
    print(keyword_list)
    if keyword_list == '':
        filter_keyword_vac_obj_list=Vacancy.filter_vacancies(sort_vac_obj_list,keyword_list)
    else:
        filter_keyword_vac_obj_list=sort_vac_obj_list
    print(f"осталось - {len(filter_keyword_vac_obj_list)} вакансий  ")




    print("Сохранимся")

    vac_dict_list = []
    for item in filter_keyword_vac_obj_list:  # сериализация в json
        vac_dict_list.append(Vacancy.vac_obj_to_dict(item))

    save = FileOperation(search_vacancy)
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