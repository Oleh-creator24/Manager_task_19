Manager_task_18  

 Реализовано  

 1. JWT-аутентификация  
- Подключена библиотека **djangorestframework-simplejwt**.  
- Эндпоинты:  
  - `POST /api/token/` — получение пары **access** и **refresh** токенов  
  - `POST /api/token/refresh/` — обновление **access** токена  
- Авторизация через заголовок:  


 2. Пермишены  
- CRUD для задач и подзадач доступен только для авторизованных пользователей.  
- Ошибка при отсутствии токена:  
```json
{ "detail": "Authentication credentials were not provided." }

3. Глобальная пагинация

Используется CursorPagination.

На одной странице отображается 5 объектов.

Пример ответа:

{
  "next": "http://127.0.0.1:8000/api/tasks/?cursor=...",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Задача 1",
      "description": "Описание",
      "deadline": "2025-10-10T12:00:00Z"
    }
  ]
}

4. Логирование

Логи сохраняются в папку logs/:

http_logs.log — HTTP-запросы

db_logs.log — SQL-запросы

Консоль — работа сервера