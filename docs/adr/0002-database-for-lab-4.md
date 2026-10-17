U
# 0002. Database for Lab 4 / База данни за Lab 4

**Status / Статус:** Accepted

## Context / Контекст

Lab 4 requires a database for storing application data. The database should be easy to configure, suitable for development and testing, and simple to use in the course environment.

Lab 4 изисква база данни за съхранение на данните на приложението. Базата данни трябва да е лесна за конфигуриране, подходяща за разработка и тестване и лесна за използване в учебната среда.

## Options / Варианти

### Option 1: SQLite

**Pros / Предимства:**
- Simple setup; no separate database server is required.
- Лесна настройка; не е необходим отделен сървър за бази данни.
- Suitable for small labs and local development.
- Подходяща за малки лабораторни задачи и локална разработка.

**Cons / Недостатъци:**
- Limited suitability for applications with many concurrent writes.
- Ограничена пригодност за приложения с много едновременни операции за запис.
- Data is stored in a local database file.
- Данните се съхраняват в локален файл.

### Option 2: PostgreSQL

**Pros / Предимства:**
- Supports concurrent users and more advanced database features.
- Поддържа едновременна работа на потребители и разширени функционалности.
- Suitable for larger applications and server deployments.
- Подходяща за по-големи приложения и сървърни среди.

**Cons / Недостатъци:**
- Requires additional setup and a running database server.
- Изисква допълнителна настройка и работещ сървър за бази данни.

- Adds configuration and maintenance overhead for a small lab.
- Добавя сложност при конфигурирането и поддръжката на малка лабораторна задача.

## Decision / Решение

Use SQLite for Lab 4 because it is easy to configure and sufficient for the expected scope of the lab.

Използваме SQLite за Lab 4, защото се конфигурира лесно и е достатъчна за очаквания обхват на лабораторната задача.

## Consequences / Последствия

- The lab can run without a separate database server.
- Лабораторната задача може да работи без отделен сървър за бази данни.
- Configuration and local development remain simple.
- Конфигурирането и локалната разработка остават лесни.
- If the application later requires more concurrent writes or server-based database features, PostgreSQL can be reconsidered.
- Ако приложението по-късно изисква повече едновременни операции за запис или функционалности на сървърна база данни, може да се обмисли PostgreSQL.
