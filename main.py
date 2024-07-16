import os
from src.file_operation import JSONData
from config import DATA_DIR

file_name = input("Введите имя файла в директории дата")
file_path = os.path.join(DATA_DIR, file_name)

data1=JSONData.load_file(JSONData(file_path))
test_list = []
print(len(data1["items"]))
for item in data1["items"]:
    test_list.append(item)
    print(item)
    print(item["area"]["name"])#city
print(type(data1))

data2=JSONData(os.path.join(DATA_DIR, "my_save.json"))
data2.write_file(test_list)