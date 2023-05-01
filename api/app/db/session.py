from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
# create tables
metadata.create_all(engine)
# reflect all tables
metadata.reflect(engine)