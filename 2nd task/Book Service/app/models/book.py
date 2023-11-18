from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.database import Base
from typing import List

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))

    # Define the relationship with the Author model
    author = relationship('Author', back_populates='books')
    transactions = relationship('Transaction', back_populates='book')


class BookCreate(BaseModel):
    title: str
    author_id: int


class BookUpdate(BaseModel):
    title: str
    author_id: int

