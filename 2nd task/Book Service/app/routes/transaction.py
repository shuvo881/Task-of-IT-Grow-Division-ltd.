from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from utils.crud import link_client_to_book, unlink_client_from_book

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def link_client_to_book_endpoint(client_id: int, book_id: int, db: Session = Depends(get_db)):
    return link_client_to_book(client_id, book_id, db)

@router.delete("/{transaction_id}")
def unlink_client_from_book_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    return unlink_client_from_book(transaction_id, db)