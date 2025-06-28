from fastapi import FastAPI
from . import models, database
from .routers import books, reviews

# ✅ Create FastAPI app
app = FastAPI(
    title="Book Review API",
    description="A simple REST API to manage books and reviews.",
    version="1.0.0"
)

# ✅ Create DB tables
models.Base.metadata.create_all(bind=database.engine)

# ✅ Include routes
app.include_router(books.router)
app.include_router(reviews.router)

# ✅ Optional: Health check endpoint
@app.get("/")
def root():
    return {"message": "Book Review API is up and running 🚀"}
