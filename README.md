# Проект: «Парсинг данных о вакансиях с hh.ru и визуализация в Power BI»
Идея: создать систему для автоматического сбора информации о вакансиях с популярного сайта hh.ru, сохранить данные в формате CSV и визуализировать их в Power BI.

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

### 3. Визуализация данных

+ **_Подготовка данных_** в Power Query и их загрузка в Power BI (замена значений ```.``` на ```,```, изменение типа данных).

+ **_Создание дашборда в Power BI._**

+ **_Настройка фильтров и параметров:_** добавление интерактивности и возможности фильтрации данных по критерию.

![image](https://github.com/user-attachments/assets/2777c638-8ed6-41c1-928a-f25dc28891f6)

### 4. Тестирование 

+ **_Проверка_** корректности работы скрипта и дашборда, выявление и исправление ошибок.

  Добавлена обработка HTTP-ошибок.

Данный проект позволит автоматизировать процесс сбора и анализа данных о вакансиях, а также предоставить удобные инструменты для исследования рынка труда и поиска работы.
