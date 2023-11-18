from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime
from jose import JWTError, jwt
from app.utils.database import get_db


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to create access token
def create_access_token(data: dict, client_id: int):
    data['client_id'] = client_id
    print(data)
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to get the current user (client) based on the access token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        client_id: int = payload.get("client_id")
        if client_id is None:
            print('Id is None')
            raise credentials_exception
        token_data = {"client_id": client_id}
    except JWTError:
        raise credentials_exception
    return token_data

