# 📚 Book Review API

A FastAPI-based backend to manage books and their reviews — built as a backend engineer assignment.

---

## 🚀 Features

- Add, list books
- Add, view reviews per book
- SQLite for DB, Redis (mocked) for caching
- Pydantic-based validation
- Fully tested with `pytest`

---

## 🧰 Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- (Mocked) Redis caching
- Pytest for testing

---

## 📁 Project Structure

book-review-service/
├── app/
│ ├── main.py # App entrypoint
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # SQLite DB setup
│ ├── cache.py # Redis (mocked) cache
│ └── routers/
│ ├── books.py # Book endpoints
│ └── reviews.py # Review endpoints
├── tests/
│ └── test_books.py # Unit + integration tests
├── requirements.txt
└── README.md


