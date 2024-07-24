import json
import os
from datetime import datetime

from config import DATA_DIR
from src.file_operation import JSONData
from src.vacancy import Vacancy, filter_vacancies


def clear_vacans():
    """загрузка файла и выделение отдельных атрибутов с сохранением в json"""
    save_file_name = datetime.now().strftime("%Y_%m_%d-%H_%M")
    print("Список файлов в папке DATA")
    m = json_file_list()
    # file_name = input("Введите имя файла в директории дата \n")
    file_index = int(input("Введите индекс файла из списка \n"))
    file_name = m[file_index]
    file_path = os.path.join(DATA_DIR, file_name)
    basename, extension = os.path.splitext(file_name)
    prof = basename.split("_")[-1]

    data1 = JSONData.load_file(JSONData(file_path))
    test_list = []
    for vacans in data1:
        test_list.append(
            {
                "id": int(vacans.get("id")),
                "name": vacans.get("name"),
                "city": vacans.get("area").get("name"),
                # "salary_from": vacans.get("salary").get("from"),
                "salary_from": (
                    vacans.get("salary").get("from")
                    if vacans.get("salary").get("from") is not None
                    else 0
                ),
                # "salary_to": vacans.get("salary").get("to"),
                "salary_to": (
                    vacans.get("salary").get("to")
                    if vacans.get("salary").get("to") is not None
                    else 0
                ),
                "url": vacans.get("url"),
                "requirement": (
                    vacans.get("snippet").get("requirement")
                    if vacans.get("snippet").get("requirement") is not None
                    else "Не указано"
                ),
                "responsibility": (
                    vacans.get("snippet").get("responsibility")
                    if vacans.get("snippet").get("responsibility") is not None
                    else "Не указано"
                ),
            }
        )

    with open(
        os.path.join(DATA_DIR, save_file_name + "_" + prof + ".vac"),
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(test_list, f, ensure_ascii=False, indent=4)


# clear_vacans()


def json_file_list():
    """функция вывода списка файлов JSON"""
    file_list = []
    for entry in os.scandir(DATA_DIR):  # вывод списка файлов
        if entry.is_dir():
            # skip directories
            continue
        elif entry.name.split(".")[-1] != "json":
            continue
        else:
            # print(entry.name)
            file_list.append(entry.name)

    for i, name_file in enumerate(file_list):
        print(i, name_file)  # вывод списка файлов JSON
    return file_list


def vac_file_list():
    """функция вывода списка файлов VAC_JSON"""
    file_list = []
    for entry in os.scandir(DATA_DIR):  # вывод списка файлов
        if entry.is_dir():
            # skip directories
            continue
        elif entry.name.split(".")[-1] != "vac":
            continue
        else:
            # print(entry.name)
            file_list.append(entry.name)

    for i, name_file in enumerate(file_list):
        print(i, name_file)  # вывод списка файлов VAC_JSON
    return file_list


# json_file_list()
# clear_vacans()
# vac_file_list()


def load_file() -> list:
    print("Список файлов в папке DATA")
    m = vac_file_list()
    # file_name = input("Введите имя файла в директории дата \n")
    file_index = int(input("Введите индекс файла из списка \n"))
    file_name = m[file_index]
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, encoding="utf-8") as json_file:
        data_list = json.load(json_file)
    return data_list


def vac_obj_from_file() -> list:
    """функция создания списка объектов класс Vacancy вакансий из vac-файла"""
    vac_list = load_file()

    new_list = []
    for item in vac_list:
        # print(item)
        # new_list.append(
        #     Vacancy(item.get("id"), item.get("name"), item.get("city"),
        #     item.get("salary_from"), item.get("salary_to"),
        #             item.get("url"), item.get("requirement"), item.get("responsibility")))
        new_list.append(Vacancy(**item))

    return new_list


# print(Vacancy.vac_list)
# filter_words = ["Python","Docker"]
# Telegram
# filter_words = ["SQL"]
new_list = vac_obj_from_file()
filter_words = input("введите ключевые слова через зпт").split(",")


print("**********************************************")
filtered_vac = filter_vacancies(new_list, filter_words)
print(f"Найдено :{len(filtered_vac)} вакансий")
for item in filtered_vac:
    print(item)
