# Название проекта: 
The LearningSystem

## Описание 
онлайн-платформа для обучения

## Установка

1. Клонируйте репозиторий

2. Установите зависимости из файла requirements.txt:
pip install -r requirements.txt

3. Настройте базу данных и сделайте миграции:
python manage.py migrate

4. Запустите сервер разработки:
python manage.py runserver

## Использование: в командной строке в виндовс выполнять запрос
Создание автора (преподавателя):
curl -X POST -H "Content-Type: application/json" -d '{"name":"Ермек"}' http://localhost:8000/users/

Создание продукта где creator id создателя продукта
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Кулинария\",\"start_date\":\"2024-03-15T00:00:00Z\",\"cost\":10.00,\"creator\":1}" http://localhost:8000/products/

Создание урока:
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Как приготовить яичницу\",\"video_link\":\"https://www.youtube.com/watch?v=abc123\",\"product\":1}" http://localhost:8000/lessons/

Создание студента:
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Иванов\"}" http://localhost:8000/users/

Можно создать больше продуктов и урроков а также студентов у каждого будет свой id