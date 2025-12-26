# FastAPI Todo Service

A simple FastAPI backend project built with a layered architecture, using SQLAlchemy ORM and Alembic for database
migrations.

---

## Tech Stack

* **Python**: 3.10+
* **Framework**: FastAPI
* **ORM**: SQLAlchemy 2.x
* **Migrations**: Alembic
* **Database**: PostgreSQL
* **ASGI Server**: Uvicorn

---

## Project Structure

```
app/
├─ controllers/      # API controllers (handle HTTP requests)
├─ services/         # Business logic layer
├─ repositories/     # Data access layer
├─ models/           # SQLAlchemy models
├─ schemas/          # Pydantic request/response schemas
├─ cores/            # Configuration, database setup, enums
├─ dependencies/     # FastAPI dependencies
├─ middlewares/      # Custom middlewares
├─ exceptions/       # Custom exceptions and handlers
├─ routers/          # API routers
├─ scripts/          # Utility and management scripts
└─ main.py           # Application entry point

alembic/             # Database migrations
```

---

## Setup

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtual environment

* **Linux / macOS**

```bash
source .venv/bin/activate
```

* **Windows**

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
fastapi dev main.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## Database Migrations

Create a new migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply migrations:

```bash
alembic upgrade head
```

---

## Notes

* Ensure PostgreSQL is running and database credentials are correctly configured in the project settings.
* This project follows a clean, layered architecture to improve maintainability and testability.
