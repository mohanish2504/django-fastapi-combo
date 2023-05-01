from fastapi import APIRouter, Depends
from app.api.deps import get_db
from app.models.book import Book

from sqlalchemy.orm import Session
router = APIRouter(prefix='/book')


@router.get("/")
def get_all_books(db:Session=Depends(get_db)):
    return db.query(Book).all()
