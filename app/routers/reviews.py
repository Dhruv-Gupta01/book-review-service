from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database, cache

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/books/{book_id}/reviews", response_model=schemas.Review)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = models.Review(**review.model_dump(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    cache.invalidate_book_reviews(book_id)
    return db_review

@router.get("/books/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    cached = cache.get_cached_reviews(book_id)
    if cached:
        return cached
    reviews = db.query(models.Review).filter(models.Review.book_id == book_id).all()
    cache.set_reviews(book_id, reviews)
    return reviews
