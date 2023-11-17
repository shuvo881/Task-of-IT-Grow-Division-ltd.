from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from utils.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)

    books = relationship("Book", back_populates="client")


class ClientCreate(BaseModel):
    full_name: str