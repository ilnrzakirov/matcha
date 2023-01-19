# matcha
Because, love too can be industrialized.


Веб приложение, сайт знакомств 


>Переменные окружения прописываются в файле .env

```
POSTGRES__HOST
POSTGRES__PORT
POSTGRES__DATABASE
POSTGRES__PASSWORD
POSTGRES__USER

UVICORN__HOST
UVICORN__PORT
```

<br/>Установка зависимостей: 

```
pip install -r requirements/requirements.txt
```

<br/>Применить миграции: 

```
make migrate
```

<br/>  Запуск

```
make run
```
