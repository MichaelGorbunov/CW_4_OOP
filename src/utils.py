import json
import os
from src.file_operation import JSONData
from config import DATA_DIR
from datetime import datetime



def clear_vacans():
    """загрузка файла и выделение отдельных атрибутов с сохранением в json"""
    save_file_name = datetime.now().strftime('%Y_%m_%d-%H_%M')

    file_name = input("Введите имя файла в директории дата \n")
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

clear_vacans()
