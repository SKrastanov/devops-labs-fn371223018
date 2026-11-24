# Service / Услугата

## Purpose / Предназначение

The Notes API allows users to create and retrieve notes through a REST API. It is used in the DevOps course to demonstrate testing, containerization, continuous integration and deployment.

## Endpoints / Адреси

| Method | Path | Description |
|---|---|---|
| GET | /health | Checks whether the service is running. |
| GET | /ready | Checks whether the storage is available. |
| GET | /version | Returns the application version. |
| GET | /notes | Returns all notes. |
| POST | /notes | Creates a new note. |
| GET | /notes/{id} | Returns a note by its ID. |
| GET | /model | Returns information about the application data model. |

## Dependencies / Зависимости

- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL when DATABASE_URL is configured
- In-memory storage when no database is configured
