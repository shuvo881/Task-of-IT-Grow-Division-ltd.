from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.utils.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    transaction_date = Column(DateTime, default=datetime.utcnow)

    # Define relationships with the Client and Book models
    client = relationship('Client', back_populates='transactions')
    book = relationship('Book', back_populates='transactions')