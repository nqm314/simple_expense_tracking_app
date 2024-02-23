.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate: 
	poetry run python -m manage migrate
.PHONY: migrations
migrations: 
	poetry run python -m manage makemigrations

.PHONY: run-server
run-server: 
	poetry run python -m manage runserver

.PHONY: superuser
superuser: 
	poetry run python -m manage createsuperuser

.PHONY: update
update: install migrate