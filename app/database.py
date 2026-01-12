from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import create_engine
from app.config import settings

Base = declarative_base()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind = engine, autoflush=False, autocommit = False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        