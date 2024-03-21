.PHONY: install
install:
	docker-compose exec web poetry install

.PHONY: build
build:
	docker-compose build

.PHONY: migrate
migrate: 
	docker-compose exec web python app/manage.py migrate
.PHONY: migrations
migrations: 
	docker-compose exec web python app/manage.py makemigrations

.PHONY: up
up: 
	docker-compose up

.PHONY: superuser
superuser: 
	docker-compose exec web python app/manage.py createsuperuser

.PHONY: update
update: install migrations migrate