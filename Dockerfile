FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py", "--start-date", "2025-06-01", "--end-date", "2025-06-07"]