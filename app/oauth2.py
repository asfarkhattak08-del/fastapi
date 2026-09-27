import time

from fastapi import Depends, HTTPException, Header,status
from . import scemha
import jwt 
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta


oauth2_scemha = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 


def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt
    
    
    
def verify_access_token(token: str, credentionals_execptions):
    
    
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)

        id: str = str(payload.get("user_id"))

        if id == None:
            raise credentionals_execptions

        token_data = scemha.TokenData(id = id)

        return token_data
    
    except: 
        raise credentionals_execptions
    

def get_current_user(token: str = Depends(oauth2_scemha)):
    credentionals_execption =  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                              detail=f" not Validete Credentionals", headers={"WWW-Authenticate": "Bearer"})
    
    return verify_access_token(token, credentionals_execption)