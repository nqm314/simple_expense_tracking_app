.PHONY: install
install:
	poetry install

.PHONY: build
build:
	docker-compose build

.PHONY: migrate
migrate: 
	docker-compose run web python app/manage.py migrate
.PHONY: migrations
migrations: 
	docker-compose run web python app/manage.py makemigrations

.PHONY: up
up: 
	docker-compose up

.PHONY: superuser
superuser: 
	poetry run python -m manage createsuperuser

.PHONY: update
update: install migrations migrate