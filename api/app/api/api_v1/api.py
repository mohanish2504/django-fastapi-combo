from fastapi import APIRouter
from app.api.api_v1.endpoints import book,author

api_router = APIRouter()
api_router.include_router(book.router,tags=['Books'])
api_router.include_router(author.router,tags=['Author'])

