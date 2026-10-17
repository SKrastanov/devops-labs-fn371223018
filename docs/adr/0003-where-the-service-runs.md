# 0003. Where the Service Runs / Къде работи услугата

**Status / Статус:** Accepted

## Context / Контекст

The service needs an environment where it can run reliably and be accessed for development, testing, and demonstration. The environment should be easy to configure and suitable for a DevOps lab.

Услугата се нуждае от среда, в която да работи надеждно и да бъде достъпна за разработка, тестване и демонстрация. Средата трябва да е лесна за конфигуриране и подходяща за лабораторна работа по DevOps.

## Options / Варианти

### Option 1: Run locally on a developer's computer

**Pros / Предимства:**
- Simple to set up and debug. / Лесна настройка и отстраняване на грешки.
- Does not require a separate hosting environment. / Не изисква отделна хостинг среда.

**Cons / Недостатъци:**
- Availability depends on the developer's computer. / Достъпността зависи от компютъра на разработчика.
- Environment differences may cause inconsistent results. / Разликите между средите могат да доведат до непоследователни резултати.

### Option 2: Run in a container

**Pros / Предимства:**
- Provides a consistent runtime environment. / Осигурява последователна среда за изпълнение.
- Can be reproduced on different machines that support containers. / Може да бъде възпроизведена на различни машини, които поддържат контейнери.

**Cons / Недостатъци:**
- Requires container configuration and a compatible runtime. / Изисква конфигурация на контейнер и съвместима среда за изпълнение.
- Adds some setup and troubleshooting overhead. / Добавя известна сложност при настройката и отстраняването на проблеми.

## Decision / Решение

Run the service in a container for the lab environment, provided the project supports container execution. This makes the runtime environment easier to reproduce and test.

За лабораторната среда услугата да работи в контейнер, при условие че проектът поддържа изпълнение в контейнер. Така средата за изпълнение се възпроизвежда и тества по-лесно.

## Consequences / Последствия

- The runtime environment can be defined and reproduced consistently. / Средата за изпълнение може да бъде описана и възпроизведена последователно.
- Developers need a compatible container runtime. / Разработчиците се нуждаят от съвместима среда за изпълнение на контейнери.
- If the project does not support containers, the decision must be revisited to match the actual deployment setup. / Ако проектът не поддържа контейнери, решението трябва да бъде преразгледано според реалната конфигурация за изпълнение.
