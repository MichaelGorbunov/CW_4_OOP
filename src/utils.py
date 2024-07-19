import json
import os
from src.file_operation import JSONData
from config import DATA_DIR
from datetime import datetime



def clear_vacans():
    """загрузка файла и выделение отдельных атрибутов с сохранением в json"""
    save_file_name = datetime.now().strftime('%Y_%m_%d-%H_%M')
    print("Список файлов в папке DATA")
    m=json_file_list()
    # file_name = input("Введите имя файла в директории дата \n")
    file_index = int(input("Введите индекс файла из списка \n"))
    file_name=m[file_index]
    file_path = os.path.join(DATA_DIR, file_name)
    basename, extension = os.path.splitext(file_name)
    prof=basename.split("_")[-1]


    data1=JSONData.load_file(JSONData(file_path))
    test_list = []
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

    with open(os.path.join(DATA_DIR, save_file_name+"_"+prof+".vac"), 'w', encoding='utf-8') as f:
        json.dump(test_list, f, ensure_ascii=False, indent=4)

# clear_vacans()

def json_file_list():
    """функция вывода списка файлов JSON"""
    file_list= []
    for entry in os.scandir(DATA_DIR):#вывод списка файлов
        if entry.is_dir():
            # skip directories
            continue
        elif entry.name.split(".")[-1] != "json":
            continue
        else:
            # print(entry.name)
            file_list.append(entry.name)

    for i, name_file in enumerate(file_list):
        print(i, name_file)#вывод списка файлов JSON
    return file_list

def vac_file_list():
    """функция вывода списка файлов VAC_JSON"""
    file_list= []
    for entry in os.scandir(DATA_DIR):#вывод списка файлов
        if entry.is_dir():
            # skip directories
            continue
        elif entry.name.split(".")[-1] != "vac":
            continue
        else:
            # print(entry.name)
            file_list.append(entry.name)

    for i, name_file in enumerate(file_list):
        print(i, name_file)#вывод списка файлов VAC_JSON
    return file_list

# json_file_list()
# clear_vacans()
vac_file_list()