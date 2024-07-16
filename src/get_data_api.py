#https://api.hh.ru/vacancies?currency=RUR&only_with_salary=true&area=113&per_page=100&text=разработчик
#https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies

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
        # return response.json()['items']
        return response.json()