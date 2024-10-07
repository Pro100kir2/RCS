FROM python:3.12.6

WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Копируем ваш скрипт в контейнер
COPY rcs.py .
# Определяем команду, которая будет выполнена при запуске контейнера
CMD ["python", "rcs.py"]