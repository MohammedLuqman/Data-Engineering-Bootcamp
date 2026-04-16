from sqlalchemy import Column, Integer ,String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key= True, index= True)
    username = Column(String ,unique= True,nullable=False ,index= True)
    email = Column(String, unique= True)
    is_active = Column(Boolean, default=True)

    projects = relationship("Project", back_populates="owner", cascade="all, delete")
    tasks = relationship("Task", back_populates="assigned_user", cascade="all, delete")