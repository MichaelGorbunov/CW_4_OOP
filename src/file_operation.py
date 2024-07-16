import os
import json
class JSONData():
    """Работа с данными в JSON файле"""

    def __init__(self, filename: str):
        self.filename = filename

    def load_file(self):
        with open(self.filename, encoding='utf-8') as json_file:
            data_list = json.load(json_file)
        return data_list

    def write_file(self, data_list: list):
        with open(self.filename, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False)