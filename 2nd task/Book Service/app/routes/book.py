from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from models.book import BookCreate, BookUpdate, Book, BookListResponse
from utils.crud import create_book, edit_book, get_books_by_filter

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=int)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)


@router.put("/{book_id}", response_model=int)
def edit_book_endpoint(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return edit_book(db, book_id, book)


@router.get("/", response_model=BookListResponse)
def list_books_endpoint(
    first_letter: str = None, author: str = None, db: Session = Depends(get_db)
):
    return get_books_by_filter(db, first_letter, author)
