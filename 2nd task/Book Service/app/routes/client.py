from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.client import ClientCreate, Client
from app.utils.crud import create_client, get_clients

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=int)
def create_client_endpoint(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)


@router.get("/", response_model=List[Client])
def list_clients_endpoint(db: Session = Depends(get_db)):
    return get_clients(db)
