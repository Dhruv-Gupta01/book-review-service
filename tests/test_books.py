from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, Base, engine
from sqlalchemy.orm import Session
import pytest
import os

client = TestClient(app)

# Optional: clean slate before tests
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Drop and recreate all tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_book():
    response = client.post("/books", json={
        "title": "Atomic Habits",
        "author": "James Clear"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Atomic Habits"
    assert data["author"] == "James Clear"
    assert "id" in data

def test_get_books():
    client.post("/books", json={"title": "Deep Work", "author": "Cal Newport"})
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_review_and_get():
    # First create book
    book = client.post("/books", json={"title": "Clean Code", "author": "Uncle Bob"}).json()
    book_id = book["id"]

    # Create review
    review_response = client.post(f"/books/{book_id}/reviews", json={
        "review_text": "Great book on writing better code.",
        "rating": 5
    })
    assert review_response.status_code == 200
    review_data = review_response.json()
    assert review_data["review_text"] == "Great book on writing better code."
    assert review_data["rating"] == 5
    assert "id" in review_data

    # Get review
    reviews = client.get(f"/books/{book_id}/reviews").json()
    assert len(reviews) == 1
    assert reviews[0]["review_text"] == "Great book on writing better code."
