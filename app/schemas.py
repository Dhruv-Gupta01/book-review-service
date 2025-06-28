from pydantic import BaseModel
from typing import List, Optional

class ReviewBase(BaseModel):
    review_text: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    model_config = {
    "from_attributes": True
}

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    reviews: List[Review] = []
    model_config = {
    "from_attributes": True
}

