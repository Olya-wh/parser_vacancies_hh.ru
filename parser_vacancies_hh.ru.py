import requests
import json
import pandas as pd
import time


def getpage(page, area):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'area': area,                   # Поиск в зоне
        'page': page,                   # Номер страницы
        'per_page': 100,                # Кол-во вакансий на 1 странице
        'text': 'Кассир, продавец',     # Поиск в полях вакансии
        #'experience': 'noExperience',  # Опыт работы
        'employment': 'full',           # Тип занятости
        'schedule': 'fullDay',          # График работы
        'only_with_salary': 1,          # Вакансии только с указанием зарплаты
        'professional_role': 97         # Профессиональная роль
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
areas_name = pd.read_csv('areas_name.txt')
areas = areas_name.area_id

for area_id in areas:
    page = 0
    time.sleep(0.5)
    while True:
        data = getpage(page, area_id)
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
all_data = all_data[['id', 'name', 'area.name', 'address.city',
                     'url', 'professional_roles', 'salary.from',
                     'salary.to', 'salary.gross', 'employer.name',
                     'experience.id']]
all_data.to_csv('vacancies_raw.csv', index=False)

print(f"Данные сохранены в файл 'vacancies_raw.csv'")

df = all_data
df['salary.from'] = df['salary.from'].fillna(df['salary.to'])
df['salary.to'] = df['salary.to'].fillna(df['salary.from'])
df['salary_avg'] = df[['salary.from', 'salary.to']].mean(axis=1)
df['salary_net'] = df.apply(
    lambda row: row['salary_avg'] * 0.87 if row['salary.gross'] else row['salary_avg'],
    axis=1)

result = df[df['area.name'].isin(areas_name.area_name)] \
  .groupby(['area.name', 'experience.id'], as_index=False) \
  .agg(salary_mean=('salary_net', 'mean'),
       salary_median=('salary_net', 'median'),
       salary_min=('salary_net', 'min'),
       salary_max=('salary_net', 'max'),
       salary_q1=('salary_net', lambda x: x.quantile(0.25)),
       salary_q3=('salary_net', lambda x: x.quantile(0.75))) \
  .sort_values(['area.name', 'salary_mean'])

result.to_csv('result.csv', index=False)

print(f"Данные сохранены в файл 'result.csv'")