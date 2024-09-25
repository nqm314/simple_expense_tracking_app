.PHONY: update
update:
	docker-compose exec web poetry update

.PHONY: freeze
freeze:
	docker-compose exec web pip freeze

.PHONY: build
build:
	docker-compose build

.PHONY: migrate
migrate: 
	docker-compose exec web python app/manage.py migrate
.PHONY: migrations
migrations: 
	docker-compose exec web python app/manage.py makemigrations BaseApp

.PHONY: up
up: 
	docker-compose up

.PHONY: superuser
superuser: 
	docker-compose exec web python app/manage.py createsuperuser

.PHONY: mg
mg: migrations migrate

.PHONY: reset
reset: 
	sudo rm -rf .venv && poetry shell && poetry install && docker-compose build --no-cache && make up