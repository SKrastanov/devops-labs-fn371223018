# Runbook

> Fill in every TODO with exact commands. / Попълнете всяко TODO с точни команди.

## Start locally / Локално стартиране

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

uvicorn app.main:app --reload
```

## Check that it works / Проверка, че работи

curl -i http://127.0.0.1:8000/health

## Run the tests / Тестове

```bash
pytest
ruff check .
```

## When something breaks / Когато нещо се счупи

python --version
which python
python -m pip check
curl -i http://127.0.0.1:8000/health

## Run with Docker

* **Build:** `docker build -t notes-api:0.3.0 .`
* **Run:** `docker run -d --name notes-app -p 8000:8000 notes-api:0.3.0`
* **Logs:** `docker logs -f notes-app`
* **Stop:** `docker stop notes-app`
