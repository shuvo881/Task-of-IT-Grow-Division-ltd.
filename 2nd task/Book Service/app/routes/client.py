from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.client import ClientCreate
from app.utils.crud import create_client, get_clients
from app.utils.security import create_access_token

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/")
def create_client_endpoint(client: ClientCreate, db: Session = Depends(get_db)):
    client_id = create_client(db, client)
    return { 'token': create_access_token(client.model_dump(), client_id)}


@router.get("/")
def list_clients_endpoint(db: Session = Depends(get_db)):
    return get_clients(db)
