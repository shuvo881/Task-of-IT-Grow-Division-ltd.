from fastapi import FastAPI
from routes import book, author, client
from utils.database import engine

app = FastAPI()

# Include routes
app.include_router(book.router)
app.include_router(author.router)
app.include_router(client.router)

# Create tables in the database
from app.models import Base

Base.metadata.create_all(bind=engine)
