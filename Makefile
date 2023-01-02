run:
	python3 run.py

makemigrations:
	alembic revision --m="$(NAME)" --autogenerate

migrate:
	alembic upgrade head