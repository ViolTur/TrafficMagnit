# Currency Tracker API

Сервіс для моніторингу курсів валют через API Monobank з фоновим оновленням даних.

## Технології
* **Django / DRF** (Backend API)
* **PostgreSQL** (Database)
* **Redis + Celery** (Background Tasks & Scheduling)
* **Docker / Docker Compose** (Containerization)

## Як запустити
1. Установіть Docker/Docker Compose
   
2. **Запустіть проект**:
   ```bash
   docker-compose up --build
   
3. **Створення адміністратора:
   Виконайте команду для доступу до панелі керування:
   
   docker exec -it "container name" python manage.py createsuperuser
   (exmpl: container name - trafficmagnit-web-1, web-1, web)
   
4. Корисні посилання

    Адмін-панель: http://127.0.0.1:8000/admin/
    (Потрібна виконати крок 3)

    Swagger UI: http://127.0.0.1:8000/api/docs/

    Redoc: http://127.0.0.1:8000/api/schema/redoc/
