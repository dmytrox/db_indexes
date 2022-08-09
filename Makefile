up:
	docker-compose up -d --build

down:
	docker-compose down

cs:
	python3 src/filldb.py

tr:
	python3 transactions.py