from sqlalchemy import Column ,String, Boolean, Integer
from app.database import Base

class Quote(Base):
    __tablename__ = "raw_quotes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quote = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    tags = Column(String, nullable=False, index=True)