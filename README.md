#  Менеджер задач (Задание №19)

##  Описание проекта
Проект **Task Manager** — это Django + DRF приложение для управления задачами и подзадачами.  
Сервис позволяет создавать, обновлять, фильтровать и отслеживать задачи с различными статусами и сроками выполнения.  

В рамках задания реализовано:
- Модели **Task**, **SubTask** и **Status**  
- API для CRUD операций  
- Подсчёт статистики и фильтрация задач  
- Поддержка сериализаторов и валидации  
- Подключение **Swagger-документации (drf-spectacular)** 

---

##  Технологии
- **Python 3.12**
- **Django 4.2**
- **Django REST Framework**
- **drf-spectacular**
- **drf-spectacular-sidecar**
- **SQLite (по умолчанию)**

---

##  Установка и запуск проекта

```bash
#  Клонировать проект
git clone https://github.com/Oleh-creator24/Manager_task_19.git
cd Manager_task_19

#  Создать виртуальное окружение и активировать его
python -m venv .venv
.venv\Scripts\activate

#  Установить зависимости
pip install -r requirements.txt
# или
pip install django djangorestframework drf-spectacular drf-spectacular-sidecar

#  Применить миграции
python manage.py migrate

#  Запустить сервер
python manage.py runserver



## Swagger документация

В проекте реализована Swagger-документация через **drf-spectacular**.

- **Swagger UI:** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **ReDoc:** [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **OpenAPI schema:** [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)