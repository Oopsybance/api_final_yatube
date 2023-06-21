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
