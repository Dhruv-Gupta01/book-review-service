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

## ✅ Features

- Add and list books with title and author
- Add and view reviews linked to specific books
- SQLite-based persistent storage
- Redis-style caching simulation for review responses
- Schema validation using Pydantic
- Modular and testable design
- Fully tested using Pytest

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-review-service.git
cd book-review-service
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Running the app

```bash
uvicorn app.main:app --reload
```


Once running, visit:

Swagger Docs: http://127.0.0.1:8000/docs
Root Health Check: http://127.0.0.1:8000


### 🧪 Running Tests

To run all unit and integration tests:
```bash
pytest
```

Expected output:

3 passed in 0.45s





### 👨‍💻 Author

Dhruv Gupta

Software Developer
📧 dhruvgupta9191@gmail.com




---

## 🌍 Live Demo

The project is deployed on **Render**.

🔗 **Live URL**: [https://book-review-service-qjwp.onrender.com/docs](https://book-review-service-qjwp.onrender.com/docs)

This link points to the interactive **Swagger UI** where you can test all API endpoints in real-time.

---
