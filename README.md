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

Используем simple jwt token полное описание есть тут https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

- получение токена - отправляем на url `http://127.0.0.1:8000/api/token/` POST запрос с  типом контента
json, c полями email, password

    Пример тела запроса
`{
    "email": "admin@ex.com",
    "password": "123"
}`
    
    Ответом будет json c двумя токенами, один для рефреша, второй для авторизации `{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5NjMwODYxMiwianRpIjoiMzFlMTdjZGJkODc1NDU5NmJhOGNhZmI2MDkyZTcwYjUiLCJ1c2VyX2lkIjoxfQ.vajxFI4egee_v1sov37VU7166mcDPj5tKJuzM3Oq3lo",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk2MjIyNTEyLCJqdGkiOiJlOGNhNGQ1OGMyMTU0Y2FjOGFiZGUwMDUyNmJjOWE5NiIsInVzZXJfaWQiOjF9.V_Wh-GxNQDJZEYcfV9vB4lb0srJpdBt7RcIeaxQoXRU"
}`

Токены имеют свойства "протухать" - наш токен закончит действовать через 3000 сек. 
   
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    
По этому нужно его обновить до истечении этого времени.
- обновление токена - отправляем POST запрос на url `http://127.0.0.1:8000/api/token/refresh/`

    пример запроса `{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5NjMwODYxMiwianRpIjoiMzFlMTdjZGJkODc1NDU5NmJhOGNhZmI2MDkyZTcwYjUiLCJ1c2VyX2lkIjoxfQ.vajxFI4egee_v1sov37VU7166mcDPj5tKJuzM3Oq3lo"
}`
    
    получаем новый токен для авторизации запросов к бэку `{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk2MjIyNTgxLCJqdGkiOiJhM2YwODgxNzk0Y2M0ODFjOTQ4ZmY5ZDkzOTAxODE5NSIsInVzZXJfaWQiOjF9.pzzZy5AghN67KFeTv_rDqh6l-QT0HlgNJc2nmD9f-zw"
}`

Дальше после получения токена можно получить например информацию о пользователе.
Отсылаем на url `http://127.0.0.1:8000/user/` POST запрос в виде: 
- в боди пишем `{
    "email": "admin@ex.com"
}`
- в хедер передаем `Authorization со значением Bearer tut_nash_token`


**Запуск сервера**

Ставим зависимости <code>pip3 install -r requirements.txt</code>

Создаем БД для разработки <code>python3 manage.py migrate</code>

Создаем админа <code>python3 manage.py createsuperuser</code>

Запускаем сервер <code>python3 manage.py runserver</code>

Сервер должен быть доступен по http://127.0.0.1:8000
Админка джанги http://127.0.0.1:8000/admin

**Routes**

Роут для регистрации пользовтаеля по инвайту `http://127.0.0.1:8000/register_user`

Отправляем туда POST запрос в котором должны быть указаны email, password, invited
выглядит это как-то так если использовтаь программу http `http POST http://127.0.0.1:8000/register_user email=user1@exam.com password=123qweASDF invite=acec2c20-3137-478f-bf5d-d94867dda427`

В ответ получите id ник пользователя, по которому потом может забрать данные пользователя (CRUD).