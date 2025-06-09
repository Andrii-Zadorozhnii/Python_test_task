# CPA Calculation ETL

## Описание
ETL-скрипт для расчета CPA (Cost Per Action) на основе данных о расходах и конверсиях.

## Быстрый запуск (3 минуты)

### Вариант 1: Локальный запуск (Poetry)

# bash
# 1. Установка Poetry
pip install poetry

# 2. Клонирование репозитория
git clone https://github.com/yourusername/cpa-calculation.git
cd cpa-calculation

# 3. Установка зависимостей
poetry install

# 4. Запуск ETL
poetry run python src/main.py --start-date 2025-06-04 --end-date 2025-06-06

### Вариант 2: Docker

# 1. Клонирование репозитория
git clone https://github.com/yourusername/cpa-calculation.git
cd cpa-calculation

# 2. Сборка и запуск
docker-compose up --build

# Или вручную:
docker build -t cpa-calculator .
docker run -v $(pwd)/data:/app/data -v $(pwd)/db:/app/db cpa-calculator

### Вариант 3: Виртуальное окружение

# 1. Создание окружения
python -m venv venv
source venv/bin/activate

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск
python src/main.py --start-date 2025-06-04 --end-date 2025-06-06


### Тестирование

pytest tests/