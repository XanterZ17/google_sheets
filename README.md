## Сводка

Скрипт для сохранения данных из Google Sheets в базу данных.  
Google таблица: https://docs.google.com/spreadsheets/d/1-2IpcuPZSHjWht5dXDnuHHknlpCN9621rY1phWnBcpg/edit#gid=0  
  
Дополнительно: Докер контейнер, telegram-bot и API на Django.  


## Скрипт

Скрипт находится в папке script.  

script.py - точка входа.  
requirements.txt - pip зависимости.  
setting.py - файл настройки, в нем находятся настройки для подключения к БД  

### Запуск

Для запсука необходимо создать виртуальное окружение, установить зависимости и убедиться,
что файл seetiing.py содержит правильные настройки для подключения к БД.

#### Setting.py

 **DB_NAME** - название базы данных.  
 **DB_USER** - пользователь базы данных, с доступом к DB_NAME.  
 **DB_PASSWORD** - пароль пользователь DB_USER.  
 **DB_HOSTNAME** - хост БД.  

#### Команды для запуска

    cd script/
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python script.py

## Docker

Папка script содержит Dockerfile  

Для корректной работы, необходимо убедиться что перед сборкой образа, файл settings.py
содержит правильные настройки для подключения к БД.  

#### Setting.py

 **DB_NAME** - название базы данных.  
 **DB_USER** - пользователь базы данных, с доступом к DB_NAME.  
 **DB_PASSWORD** - пароль пользователь DB_USER.  
 **DB_HOSTNAME** - хост БД.  

## Django

 Back-end сервер выполнен с использованием Django и Django REST Framework  

 API имеет следующие эндпоинты:  
   /api/test - все записи из таблицы test  
 
 Насйтроки для доступа к базе содержаться в следующих файлах:  
 ~/.pg_service.conf  
 ~/.gsb_pgpass  

## Telegram Bot

Для запуска необходимо установить зависимости из файла requirements.txt, и отредоктировать файл settings.py

#### Setting.py

 **DB_NAME** - название базы данных.  
 **DB_USER** - пользователь базы данных, с доступом к DB_NAME.  
 **DB_PASSWORD** - пароль пользователь DB_USER.  
 **DB_HOSTNAME** - хост БД.  
  
 **API_KEY** - API ключ telegram бота