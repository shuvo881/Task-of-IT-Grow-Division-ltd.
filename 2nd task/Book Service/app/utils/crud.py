from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.book import Book, BookCreate, BookUpdate
from app.models.author import Author, AuthorCreate
from app.models.client import Client, ClientCreate
from app.models.transaction import Transaction

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.model_dump())
    print(db_book)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book.id

def edit_book(db: Session, book_id: int, book: BookUpdate):
    # Step 1: Retrieve the book from the database
    db_book = db.query(Book).filter(Book.id == book_id).first()

    # Step 2: Check if the book exists
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    # Step 3: Update the book attributes based on the values provided
    for field, value in book.model_dump_json().items():
        setattr(db_book, field, value)  # Update the book attribute with the new value

    # Step 4: Commit the changes to the database
    db.commit()

    # Step 5: Return the updated book
    return db_book

def get_books_by_filter(db: Session, title_startswith: str = None, author_id: int = None):
    query = db.query(Book)

    if title_startswith:
        query = query.filter(Book.title.startswith(title_startswith))

    if author_id:
        query = query.filter(Book.author_id == author_id)

    books = query.all()
    return books

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author.id

def get_authors(db: Session):
    return db.query(Author).all()

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client.id

def get_clients(db: Session):
    return db.query(Client).all()


# Link a client to a book (client borrowed the book)
def link_client_to_book(client_id: int, book_id: int, db: Session):
    client = db.query(Client).filter(Client.id == client_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()

    if client is None or book is None:
        raise HTTPException(status_code=404, detail="Client or book not found")

    transaction = Transaction(client_id=client_id, book_id=book_id)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


# Unlink a client from a book (client returned the book)
def unlink_client_from_book(transaction_id: int, db: Session):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted"}