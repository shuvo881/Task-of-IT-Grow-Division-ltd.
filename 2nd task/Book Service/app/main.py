from fastapi import FastAPI
from app.routes import book, author, client, transaction
from app.utils.database import engine
from app import models

app = FastAPI()

# Include routes
app.include_router(book.router)
app.include_router(author.router)
app.include_router(client.router)
app.include_router(transaction.router)


# Create tables in the database
models.book.Base.metadata.create_all(bind=engine)
models.author.Base.metadata.create_all(bind=engine)
models.client.Base.metadata.create_all(bind=engine)
models.transaction.Base.metadata.create_all(bind=engine)
