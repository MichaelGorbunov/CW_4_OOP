# https://api.hh.ru/vacancies?currency=RUR&only_with_salary=true&area=113&per_page=100&text=разработчик
# https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies

import requests


# class HeadHunterAPI():
#     """Работа с API платформы HeadHunter"""
#
#     # def __init__(self, keyword: str):
#     def __init__(self):
#         self.url = 'https://api.hh.ru/vacancies'
#         self.params = {
#             # 'text': "keyword",
#             'area': 113,
#             'only_with_salary': True,
#             'page': 0,
#             'per_page': 100,
#         }
#
#     def get_vacancies(self, keyword: str):
#         """Возвращает вакансии по заданному параметру"""
#         self.params["text"] = keyword
#
#         response = requests.get(self.url, params=self.params)
#         # return response.json()['items']
#         return response.json()



import requests
class HeadHunterAPI():
    """Работа с API платформы HeadHunter"""
    def __init__(self, keyword: str):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': keyword,
            'area': 113,
            'only_with_salary': True,
            'page': 0,
            'per_page': 100,
            }

    def get_vacancies(self):
        """Возвращает вакансии по заданному параметру"""

        response = requests.get(self.url, params=self.params)
        return response.json()['items']
        # return response.json()

# class HH(Parser):
#     """ Класс для работы с API HeadHunter """
#     def __init__(self):
#         self.url: str = 'https://api.hh.ru/vacancies'
#         self.headers: dict = {'User-Agent': 'HH-User-Agent'}
#         self.params: dict = {'text': '', 'page': 0, 'per_page': 100}
#         self.vacancies: list = []
#         print("Загрузка данных с ресурса HH.ru. Ждите.")
#
#     def load_vacancies(self, keyword: str):
#         """ Метод для получения данных с ресурса HH.ru """
#         self.params['text'] = keyword
#         while self.params.get('page') != 20:
#             response = requests.get(self.url, headers=self.headers, params=self.params)
#             vacancies = response.json()['items']
#             self.vacancies.extend(vacancies)
#             self.params['page'] += 1
#         return self.vacancies
