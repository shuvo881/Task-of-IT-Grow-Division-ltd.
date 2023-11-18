from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.book import BookCreate, BookUpdate, Book
from app.utils.crud import create_book, edit_book, get_books_by_filter

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)


@router.put("/{book_id}")
def edit_book_endpoint(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return edit_book(db, book_id, book)


@router.get("/")
def list_books_endpoint(
    first_letter: str = None, author: str = None, db: Session = Depends(get_db)
):
    return get_books_by_filter(db, first_letter, author)
