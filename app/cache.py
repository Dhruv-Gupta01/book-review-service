import fakeredis
import json
from .schemas import Review

r = fakeredis.FakeStrictRedis()

def _key(book_id: int):
    return f"reviews:{book_id}"

def set_reviews(book_id: int, reviews):
    data = [Review.from_orm(r).__dict__ for r in reviews]
    r.set(_key(book_id), json.dumps(data))

def get_cached_reviews(book_id: int):
    raw = r.get(_key(book_id))
    if raw:
        data = json.loads(raw)
        return [Review(**r) for r in data]
    return None

def invalidate_book_reviews(book_id: int):
    r.delete(_key(book_id))
