## Стек технологий  

<img src="https://img.shields.io/badge/Python - black?style=for-the-badge&logo=Python&logoColor=blue"/> <img src="https://img.shields.io/badge/Flask - black?style=for-the-badge&logo=Flask&logoColor=white"/> <img src="https://img.shields.io/badge/SQLAlchemy - black?style=for-the-badge"/> <img src="https://img.shields.io/badge/sqlite - black?style=for-the-badge&logo=sqlite&logoColor=blue"/>


## Установка проекта локально (Linux)  
+ Склонировать репозиторий и перейти в него в командной строке:  
```
git clone https://github.com/lobster2nd/Bookstore.git  
cd Bookstore
```  
+ Cоздать и активировать виртуальное окружение:   
```
python -m venv env
```  
```
source env/bin/activate
```  
+ Перейти в директорию и установить зависимости из файла requirements.txt:  
```
pip install -r requirements.txt
```  
+ Выполнить команду:  
```
python3 flask --app bookstore --debug run
```  

Endpoints:  
`http://127.0.0.1:5000/books/` - GET - список книг  
`http://127.0.0.1:5000/books/<id>/` - DELETE - удалить книгу по ID  
`http://127.0.0.1:5000/books/` - POST - добавить книку. Формат: {"title": "string", "description": "string", "publish_year": "integer", "pages_count": "integer", "created_at": "YYYY-MM-DD"}  

