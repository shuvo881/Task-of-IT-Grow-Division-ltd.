from fastapi import FastAPI
from routes import book, author, client
from utils.database import engine
import models

app = FastAPI()

# Include routes
app.include_router(book.router)
app.include_router(author.router)
#app.include_router(client.router)

# Create tables in the database

models.book.Base.metadata.create_all(bind=engine)
models.author.Base.metadata.create_all(bind=engine)
models.client.Base.metadata.create_all(bind=engine)
