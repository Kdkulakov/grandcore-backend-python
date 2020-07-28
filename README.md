# grandcore-backend-python

Используем Django 3 + DRF + JWT tokes

Основной URL работы с пользователями /user/. По данному урлу можно получить:
* сипсок пользователей
* конкретного юзера по ID
* добавить пользователя
* удаление пользователя
* редактирование пользователя

Корень сервера - это список доступных URL для работы с API. Можно прям в WEB интерфейсе поиграться с API шкой.

**Безопасность**

Используем jwt token полное описание есть тут https://jpadilla.github.io/django-rest-framework-jwt/

Тут все стандартно/по инструкции

**Запуск сервера**

Ставим зависимости <code>pip3 install -r requirements.txt</code>

Создаем БД для разработки <code>python3 manage.py migrate</code>

Создаем админа <code>python3 manage.py createsuperuser</code>

Запускаем сервер <code>python3 manage.py runserver</code>

Сервер должен быть доступен по http://127.0.0.1:8000
Админка джанги http://127.0.0.1:8000/admin