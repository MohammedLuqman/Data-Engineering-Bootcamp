from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy_utils import database_exists,create_database

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/Luqman"

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)   

engine = create_engine(DATABASE_URL, echo= False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
