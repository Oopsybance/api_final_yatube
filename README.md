# Yatube API

API для социальной сети Yatube, где пользователи могут создавать посты, оставлять комментарии и подписываться на других пользователей.

## Используемые технологии
Python 3.9
Django
Django REST Framework
pytest
pytest-django
python-decouple

## Установка

1. Клонируйте репозиторий по ссылке:
https://github.com/Oopsybance/api_final_yatube

2. Установите виртуальное окружение командой:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
- На Windows:
```bash
source venv/Scripts/activate
```
- На Unix или MacOS:
```bash
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Создайте файл .env в корневом каталоге и установите ваши переменные окружения:
```bash
SECRET_KEY=your-secret-key
```

6. Выполните миграции:
```bash
python manage.py migrate
```

7. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

8. Запускаем проект:
```bash
python manage.py runserver
```


## Использование

API поддерживает следующие запросы:

* `GET api/v1/posts/` - Получение списка всех постов.
* `POST api/v1/posts/` - Создание нового поста (требуется аутентификация).
* `GET api/v1/posts/{post_id}/` - Получение информации о конкретном посте.
* `PUT, PATCH api/v1/posts/{post_id}/` - Обновление поста (требуется аутентификация и авторство поста).
* `DELETE api/v1/posts/{post_id}/` - Удаление поста (требуется аутентификация и авторство поста).
* `GET api/v1/groups/` - Получение списка всех групп.
* `POST api/v1/follow/` - Подписаться на другого пользователя (требуется аутентификация).
* `GET api/v1/follow/` - Получить список подписок (требуется аутентификация).


## Аутентификация

Для аутентификации используются JWT-токены. Получить токен можно, сделав POST-запрос на эндпоинт `/v1/auth/jwt/create/` с данными пользователя в теле запроса.

После аутентификации токен должен быть включен в заголовки всех запросов, требующих аутентификации, в формате: `Authorization: Bearer {your_token}`.


## Примеры запросов к API

- Создание нового поста:
Запрос:
POST api/v1/posts/
Authorization: Bearer {your_token}
{
  "text": "Hello, world!"
}

Ответ:
{
  "id": 1,
  "author": "Misha",
  "text": "Hello, world!",
  "pub_date": "2023-06-22T10:20:30Z"
  "group": null,
  "image": null,
}

- Подписка на другого пользователя
Запрос:
POST api/v1/follow/
Authorization: Bearer {your_token}
{
  "following": "other_username"
}
Ответ:
{
    "user": "Misha",
    "following": "Aleftina"
}
