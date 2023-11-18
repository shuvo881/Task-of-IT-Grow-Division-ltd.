from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.utils.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)

    transactions = relationship('Transaction', back_populates='client')


class ClientCreate(BaseModel):
    full_name: str
