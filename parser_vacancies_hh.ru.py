import requests
import json
import pandas as pd

def getPage(page, area):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'area': area,                   # Поиск в зоне
        'page': page,                   # Номер страницы
        'per_page': 100,                # Кол-во вакансий на 1 странице
        'text': 'Аналитик данных',      # Поиск в полях вакансии
        #'experience': 'noExperience',  # Опыт работы
        'employment': 'full',           # Тип занятости
        'schedule': 'fullDay',          # График работы
        'only_with_salary': 1,          # Вакансии только с указанием зарплаты
        'professional_role': 10         # Профессиональная роль
    }
    try:
        req = requests.get(url, params)
        req.raise_for_status()  # Вызовет исключение для HTTP ошибок
        data = req.content.decode()
        req.close()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

all_data = pd.DataFrame()
page=0

while True:
    data = getPage(page, 1)
    if data is None:
        break
    parsed_data = json.loads(data)  # Парсим JSON
    if (parsed_data['found']/100) <= page:
        break
    page += 1
    items = parsed_data['items']  # Извлекаем items
    new_df = pd.json_normalize(items)  # Преобразуем в DataFrame
    all_data = pd.concat([all_data, new_df])  # Объединяем с текущим DataFrame

#преобразуем данные в CSV
all_data = all_data[['id','name','url','professional_roles','salary.from','salary.to','employer.name','experience.id']]
all_data.to_csv('vacancies_raw.csv', index=False)

print(f"Данные сохранены в файл 'vacancies_raw.csv'")