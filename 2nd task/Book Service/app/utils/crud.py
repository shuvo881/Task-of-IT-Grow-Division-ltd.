from sqlalchemy.orm import Session
from models.book import Book, BookCreate, BookUpdate
from models.author import Author, AuthorCreate
from models.client import Client, ClientCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book.id

def edit_book(db: Session, book_id: int, book: BookUpdate):
    # Implement the logic to edit the book
    pass

def get_books_by_filter(db: Session, first_letter: str = None, author: str = None):
    # Implement the logic to get books based on filters
    pass

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
