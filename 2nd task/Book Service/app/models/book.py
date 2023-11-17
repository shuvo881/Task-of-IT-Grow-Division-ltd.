from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utils.database import Base
from typing import List

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")


class BookCreate(BaseModel):
    title: str
    author_id: int


class BookUpdate(BaseModel):
    title: str
    author_id: int

class BookListResponse(BaseModel):
    items: List[Book]

    class Config:
        orm_mode = True
