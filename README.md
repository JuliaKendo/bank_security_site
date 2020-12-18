# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка. Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы к БД. 

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников банка.

## Переменные окружения

`DB_HOST` - адрес хоста.

`DB_PORT` - порт хоста.

`DB_NAME` - имя базы данных.

`DB_USER` - имя пользователя базы данных.

`DB_PASSWORD` - пароль пользователя базы данных.

`SECRET_KEY` - секретный токен.

`DEBUG` - режим отладки Django.

## Установка

Python3 должен быть установлен.

1. Заполнить переменные окружения.

2. Установить зависимости:

```
pip install -r requirements.txt
```

## Запуск

```
python.exe manage.py runserver 0.0.0.0:8000
```	
В браузере - [http://0.0.0.0](http://0.0.0.0:8000)


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
