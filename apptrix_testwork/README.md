# Тестовое задание для Apptrix

## Задачи:

1) [Создать модель участников. У участника должна быть аватарка, пол, имя и фамилия, почта.]

2) [Создать эндпоинт регистрации нового участника: /api/clients/create (не забываем о пароле и совместимости с авторизацией модели участника)]

3) [При регистрации нового участника необходимо обработать его аватарку: наложить на него водяной знак (в качестве водяного знака можете взять любую картинку).]

4) [Создать эндпоинт оценивания участником другого участника: /api/clients/{id}/match. В случае, если возникает взаимная симпатия, то ответом выдаем почту клиенту и отправляем на почты участников: «Вы понравились <имя>! Почта участника: <почта>».]

5) [Создать эндпоинт списка участников: /api/list. Должна быть возможность фильтрации списка по полу, имени, фамилии. Советую использовать библиотеку Django-filters.]

6) [Реализовать определение дистанции между участниками. Добавить поля долготы и широты. В api списка добавить дополнительный фильтр, который показывает участников в пределах заданной дистанции относительно авторизованного пользователя. Не забывайте об оптимизации запросов к базе данных
https://en.wikipedia.org/wiki/Great-circle_distance]

7) [Задеплоить проект на любом удобном для вас хостинге, сервисах PaaS (Heroku) и т.п. Должна быть возможность просмотреть реализацию всех задач. Если есть какие-то особенности по тестированию, написать в Readme. Там же оставить ссылку/ссылки на АПИ проекта](http://russianprogram.pythonanywhere.com/api/clients/)
## http://russianprogram.pythonanywhere.com/api/clients/

# HOW TO:
## Как запустить на Локалке
### Клонируем
```
git clone https://github.com/RussianProgram/apptrix_testwork.git
```
### Первоначальная установка 
```
cd apptix_testwork
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```
Создаём супер-юзера с именем admin и паролем admin.

# API DOCUMENTATION:
### CLIENTS LIST (GET)
```shell
curl --location --request GET http://localhost:8000/api/clients/
```
### CLIENTS LIST WITH FILTERS (GET)
#### Отоброзить пользователей женского пола в радиусе 500 метров(вычисляется на основании долготы и широты)
```shell
curl --location --request GET http://localhost:8000/api/clients/?sex="F"&distance=500
```
### CREATE CLIENT (POST)
```shell
curl --data "username=somename&password=somepass&password2=somepass&email=email&first_name=name&last_name=name" http://localhost:8000/api/clients/
```
### CLIENT DETAIL (GET)
```shell
curl --location --request GET http://localhost:8000/api/clients/{client_id}/
```
### CLIENT UPDATE (PUT) 
#### Authentification only!
```shell
curl --data "{"sex":"F""}" http://localhost:8000/api/clients/{client_id}/
```
### CLIENT MATCH (GET)
#### Authentification only!
```shell
curl --location --request GET http://localhost:8000/api/clients/{client_id}/match/
```
