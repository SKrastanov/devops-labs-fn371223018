# Runbook

> Fill in every TODO with exact commands. / Попълнете всяко TODO с точни команди.

## Start locally / Локално стартиране

python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload

## Check that it works / Проверка, че работи

Open http://127.0.0.1:8000/health. You should see `{"status":"ok"}`. The API documentation is at http://127.0.0.1:8000/docs. / Отворете http://127.0.0.1:8000/health. Трябва да видите `{"status":"ok"}`. Документацията на API е на http://127.0.0.1:8000/docs.

## Run the tests / Тестове

```bash
pytest
```

## When something breaks / Когато нещо се счупи

1. Check that the app responds; expect HTTP 200 and `{"status":"ok"}`. / Проверете дали приложението отговаря; очаквайте HTTP 200 и `{"status":"ok"}`.

	```bash
	curl -i http://127.0.0.1:8000/health
	```

2. Check the Python version and that the app dependencies are installed. / Проверете версията на Python и дали зависимостите са инсталирани.

	```bash
	python --version
	python -m pip show fastapi uvicorn
	```

3. Run the test suite to find regressions. / Стартирайте тестовете, за да откриете регресии.

	```bash
	pytest
	```
