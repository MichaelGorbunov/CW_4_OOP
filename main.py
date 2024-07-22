import json
import os
from src.file_operation import JSONData
from config import DATA_DIR
from src.get_data_api import HeadHunterAPI
from datetime import datetime

save_file_name = datetime.now().strftime('%Y_%m_%d-%H_%M')
def func1():
    #чистка файла

    file_name = input("Введите имя файла в директории дата")
    file_path = os.path.join(DATA_DIR, file_name)

    data1=JSONData.load_file(JSONData(file_path))
    test_list = []
    # print(len(data1["items"]))
    # for item in data1["items"]:
    #     test_list.append(item)
    #     print(item)
    #     print(item["area"]["name"])#city
    # print(type(data1))
    #2024_07_16-15_12_программист.json
    #2024_07_16-14_57_Разработчик Python.json


    for vacans in data1:
                test_list.append(
                    {
                        "id": int(vacans.get("id")),
                        "name": vacans.get("name"),
                        "city": vacans.get("area").get("name"),
                        "salary_from": vacans.get("salary").get("from"),
                        "salary_to": vacans.get("salary").get("to"),
                        "url": vacans.get("url"),
                        "requirement": vacans.get("snippet").get("requirement"),
                        "responsibility": vacans.get("snippet").get("responsibility")
                    }
                )

    # data2=JSONData(os.path.join(DATA_DIR, "my_save.json"))
    # data2.write_file(test_list)
    with open(os.path.join(DATA_DIR, save_file_name+".vac"), 'w', encoding='utf-8') as f:
        json.dump(test_list, f, ensure_ascii=False, indent=4)


def func2():

    # получение данных из api
    search_vacancy = input('Введите запрос:\n')
    data1=HeadHunterAPI.get_vacancies(HeadHunterAPI(search_vacancy))

    test_list = []
    print(len(data1))
    for item in data1:
        test_list.append(item)
        print(item)
        print(item["area"]["name"])#city
    print(type(data1))

    # data2=JSONData(os.path.join(DATA_DIR, save_file_name+"_"+search_vacancy+".json"))
    # data2.write_file(test_list)
    with open(os.path.join(DATA_DIR, save_file_name+"_"+search_vacancy+".json"), 'w', encoding='utf-8') as f:
        json.dump(test_list, f, ensure_ascii=False, indent=4)


#
# for fname in os.listdir(DATA_DIR):
#     print(fname)
#     path = os.path.join(DATA_DIR, fname)
#     if os.path.isdir(DATA_DIR):
#         # skip directories
#         continue
#     print(fname)


# for entry in os.scandir(DATA_DIR):#вывод списка файлов
#     if entry.is_dir():
#         # skip directories
#         continue
#     else:
#         print(entry.name)


func2()