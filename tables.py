from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """State Class"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255))
