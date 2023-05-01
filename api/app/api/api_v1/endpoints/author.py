from fastapi import APIRouter, Depends
from app.api.deps import get_db

from app.models.author import Author
from sqlalchemy.orm import Session
router = APIRouter(prefix='/author')



@router.get("/")
def get_all_author(db:Session=Depends(get_db)):
    return db.query(Author).all()