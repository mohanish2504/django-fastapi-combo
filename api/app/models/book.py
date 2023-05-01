from app.db.session import engine,metadata
from app.db.base import Base
from sqlalchemy import Table

book_table = Table('book_book',metadata,autoload_with=engine)
class Book(Base):
    __table__ = book_table