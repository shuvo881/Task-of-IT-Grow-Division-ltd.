from app.models.client import Client
from app.utils.security import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.crud import link_client_to_book, unlink_client_from_book

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def link_client_to_book_endpoint(book_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    client_id = current_user.get("client_id")
    
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return link_client_to_book(client_id, book_id, db)

@router.delete("/{transaction_id}")
def unlink_client_from_book_endpoint(transaction_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    client_id = current_user.get("client_id")
    
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    
    return unlink_client_from_book(transaction_id, db)