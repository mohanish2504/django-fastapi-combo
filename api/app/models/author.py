from app.db.session import metadata,engine
from app.db.base import Base
from sqlalchemy import Table

author_table = Table('book_author',metadata,autoload_with=engine)
class Author(Base):
    __table__ = author_table