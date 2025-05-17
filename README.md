# Проект: «Парсинг данных о вакансиях с hh.ru»
Идея: создать систему для автоматического сбора информации о вакансиях с популярного сайта hh.ru, рассчитать основные показатели мониторинга зарплат и сохранить данные в формате CSV.

## Описание проекта:

### 1. Подготовка и планирование

+ **_Выбор инструментов:_** Python для парсинга данных, Power BI для визуализации.

+ **_Изучение API hh.ru:_** анализ документации и примеров использования API для получения доступа к данным о вакансиях.

  Основные параметры, используемые в запросе

  ```area```:Поиск в зоне
  
  ```page```:Номер страницы

  ```per_page```:Кол-во вакансий на 1 странице
  
  ```text```:Поиск в полях вакансии
  
  ```experience```:Опыт работы
  
  ```employment```:Тип занятости
  
  ```schedule```:График работы
  
  ```only_with_salary```:Вакансии только с указанием зарплаты
  
  ```professional_role```:Профессиональная роль

+ **_Проектирование структуры данных:_** определение формата хранения данных (CSV). 

### 2. Парсинг данных 

+ **_Написание скрипта на Python:_** создание скрипта для извлечения данных о вакансиях с использованием библиотек для работы с API и таблицами (```requests```, ```json```, ```pandas```). 

+ **_Обработка данных:_** очистка и преобразование данных в нужный формат.

>  На выходе получится таблица со следующими колонками: _id, premium, name, department, has_test,  response_letter_required, response_url, sort_point_distance, published_at, created_at, archived, apply_alternate_url, show_logo_in_search, insider_interview, url, alternate_url, relations, contacts, working_days, working_time_intervals, working_time_modes, accept_temporary, professional_roles, accept_incomplete_resumes, adv_response_url, is_adv_vacancy, adv_context, area.id, area.name, area.url, salary.from, salary.to, salary.currency, salary.gross, type.id, type.name, address.city, address.street, address.building, address.lat, address.lng, address.description, address.raw, address.metro, address.metro_stations, address.id, branding.type, branding.tariff, employer.id, employer.name, employer.url, employer.alternate_url, employer.logo_urls.original, employer.logo_urls.90, employer.logo_urls.240, employer.vacancies_url, employer.accredited_it_employer, employer.trusted, snippet.requirement, snippet.responsibility, schedule.id, schedule.name, experience.id, experience.name, employment.id, employment.name, address.metro.station_name, address.metro.line_name, address.metro.station_id, address.metro.line_id, address.metro.lat, address.metro.lng, address, employer.logo_urls, department.id, department.name._

  Для анализа зарплат понадобятся следующие данные: ```salary.from```, ```salary.to```, ```experience.id```.

+ **_Сохранение данных:_** запись обработанных данных в CSV файл для дальнейшего использования.

### 3. Анализ зарплатных показателей

+ **Для каждого города и уровня опыта выводится:**

  Распределение зарплат: Минимум (min), максимум (max), квартили (q1, q3).

  Центральные тенденции: Среднее (mean) и медианное (median) значение зарплат.

  Данные очищены от пропусков и скорректированы на налоги.

Готовые данные можно использовать для визуализации (например, boxplot по городам).

```
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 24))

# Построение boxplot
ax = sns.boxplot(
    y='area.name',
    x='salary_net',
    data=resulte,
    fliersize=3,
    showmeans=True,
    meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black"})

# Заголовки и подписи
plt.title("Распределение зарплат (нетто) по городам", 
    fontsize=16, pad=20)
plt.xlabel("Зарплата (нетто)", fontsize=12)
plt.ylabel("Город", fontsize=12)

# Настройка сетки, шрифтов, отображения
ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine(left=True)
plt.tight_layout()  

plt.show()
```

![Распределение зарплат (нетто) по городам](https://github.com/user-attachments/assets/19ac552f-7090-49f5-a150-1c91855c16b3)


### 4. Тестирование 

+ **_Проверка_** корректности работы скрипта, выявление и исправление ошибок.

  Добавлена обработка HTTP-ошибок.

Данный проект позволит автоматизировать процесс сбора и анализа данных о вакансиях, а также предоставить удобные инструменты для исследования рынка труда и поиска работы.
