.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate: 
	poetry run python -m app.manage migrate
.PHONY: migrations
migrations: 
	poetry run python -m app.manage makemigrations

.PHONY: run-server
run-server: 
	poetry run python -m app.manage runserver

.PHONY: superuser
superuser: 
	poetry run python -m app.manage createsuperuser

.PHONY: update
update: install migrate