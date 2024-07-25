import json
import os
from datetime import datetime
from config import DATA_DIR
from src.vacancy import Vacancy


class FileOperation:
    """Работа с файлами"""

    def __init__(self, filename: str):
        # if filename is None:
        #     filename = datetime.now().strftime("%Y_%m_%d-%H_%M")
        self.filename = filename+"_"+datetime.now().strftime("%Y_%m_%d-%H_%M")

    def load_file(self):
        with open(self.filename, encoding="utf-8") as json_file:
            data_list = json.load(json_file)
        return data_list

    def write_file(self, data_list: list):
        with open(
                os.path.join(DATA_DIR, self.filename + ".vac"),
                "w",
                encoding="utf-8",
        ) as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)


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


def vac_obj_from_file() -> list:
    """функция создания списка объектов класс Vacancy вакансий из vac-файла"""
    vac_list = load_file()
    vac_obj_list = []
    for item in vac_list:
        vac_obj_list.append(Vacancy(**item))
    return vac_obj_list


def load_file() -> list:
    """метод выбора файла в папке DATA и его чтения """
    print("Список файлов в папке DATA")
    file_list = vac_file_list()
    if len(file_list) == 0:
        print("файлов не найдено")
        return [''],""
    # file_name = input("Введите имя файла в директории дата \n")
    file_index = int(input("Введите индекс файла из списка \n"))
    file_name = file_list[file_index]
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, encoding="utf-8") as json_file:
        data_list = json.load(json_file)
    return data_list,file_name



