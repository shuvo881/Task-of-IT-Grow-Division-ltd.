from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.author import AuthorCreate, Author
from app.utils.crud import create_author, get_authors

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.post("/")
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)


@router.get("/")
def list_authors_endpoint(db: Session = Depends(get_db)):
    return get_authors(db)
