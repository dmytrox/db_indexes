up:
	docker-compose up -d --build

down:
	docker-compose down

run:
	python3 src/filldb.py
	python3 transactions.py