# app_name Service


## Description
`app_name-service` is a Python-based API project built using FastAPI, a high-performance web framework for creating RESTful APIs. This project provides a solid foundation and structure to develop scalable and maintainable APIs.

It based on **Clean Architecture**, **Hexagonal architecture**, **SOLID principles** and **Onion architecture**.


## Installation

```
python3 -m venv venv
source venv/bin/activate
# source venv/Scripts/activate - Windows
pip install -r requirements.txt`
```

## Docker: Run Project

### Run build container

```bash
docker build -t app_name-service .
```

### Run  the container

```bash
docker-compose up --force-recreate --build

# check sql container
docker-compose exec db psql --username=app_name --dbname=app_name_service # env variables
```

With the **docker-compose** configuration, this generate a API endpoint in the port 8000. You can access to the API in the following URL: http://localhost:8000

### Migrations

The project uses Alembic to manage database migrations. Alembic is a lightweight database migration tool for SQLAlchemy.

```bash
Terminal 1:
docker-compose up

Terminal 2:
docker-compose exec app bash
#Generate migration
alembic revision --autogenerate -m "migration message"
#Apply migration
alembic upgrade head
```
***Note**: If you only want to run the migrations, you can use the following command*

```bash
docker-compose exec app alembic upgrade head
```

The project uses a PostgreSQL database. You can access the database using the following command:

```bash
docker-compose exec db psql --username=app_name --dbname=app_name_service
```

### Run tests

```bash
Terminal 1:
docker-compose up

Terminal 2:
docker-compose exec api bash
python -m pytest
```


## Project Structure
```bash
fast-api-base
├─ .gitignore
├─ app
│  ├─ adapter
│  │  ├─ async_tasks.py
│  │  └─ __init__.py
│  ├─ database
│  │  └─ __init__.py
│  ├─ domain
│  │  └─ __init__.py
│  ├─ infrastructure
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ schemas
│  │  ├─ request.py
│  │  └─ response.py
│  ├─ service
│  │  └─ __init__.py
│  ├─ settings.py
│  ├─ tests
│  │  ├─ test_app.py
│  │  └─ __init__.py
│  └─ utils
│     ├─ custom_http_response.py
│     └─ tools.py
├─ scripts
│  └─ extract_openapi.py
├─ docker-compose.yml
├─ Dockerfile
├─ pytest.ini
├─ README.md
├─ requirements.txt
├─ start-container.sh
└─ supervisord.conf
```

## Scaffolding and Architecture

The project follows a well-organized directory structure:

**app**: This directory contains the main app-related code.

**adapter**: Contains files that connect the service with external services from infrastructure.

**database**: Directory that potentially holds code related to database configuration, connections and models.

**domain**: Contains files representing the project's domain logic.

**infrastructure**: Contains files managing the technical infrastructure of the application.

**main.py**: The main app file where the FastApi application is defined and configured.

**schemas**: Contains data schemas used for app incoming requests and outgoing responses.

**service**: Contains files connect the domain with particular uses cases for the app.

**settings.py**: File to store app configuration, such as environment variables, etc.

**tests**: Directory for automated app tests.

**utils**: Contains utility functions or common tools used in the application.

**scripts**: Contains scripts to help with the development process.

**Note**: These articles is based on the following: 

- [Hexagonal Architecture](https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63).
- [FastAPI with Ormar, Docker and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/).

**References**: Inspired by [refactoring](https://refactoring.guru/es/design-patterns/), [12factor](https://12factor.net/es/)
