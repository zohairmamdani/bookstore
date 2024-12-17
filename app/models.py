from sqlalchemy import Column, Integer, String
from .database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    published_year = Column(Integer, nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
