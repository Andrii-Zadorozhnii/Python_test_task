init:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

run:
	./venv/bin/python src/main.py --start-date 2025-06-04 --end-date 2025-06-06

test:
	pytest tests/

docker-build:
	docker build -t cpa-calculator .

docker-run:
	docker run -v $(pwd)/data:/app/data -v $(pwd)/db:/app/db cpa-calculator

compose-up:
	docker-compose up --build