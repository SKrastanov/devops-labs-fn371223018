# Service / Услугата

> Fill in every TODO. / Попълнете всяко TODO.

## Purpose / Предназначение

TODO: two or three sentences: what the service does and for whom. / две-три изречения: какво прави услугата и за кого.

## Endpoints / Адреси

| Method | Path | What it does / Какво прави |
|---|---|---|
| GET | /health | Checks whether the service is running. |
| GET | /version | Returns the current version of the service. |
| GET | /notes | Returns the list of all notes. |
| POST | /notes |  Creates a new note |
| GET | /notes/{id} | Returns the note with the specified ID. |

## Dependencies / Зависимости

The service provides a REST API for managing notes. It allows users to retrieve all notes, create new notes, and retrieve individual notes by their ID. It also provides health and version endpoints to check the service status and current version.