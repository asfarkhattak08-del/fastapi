from fastapi import APIRouter, Depends , status, HTTPException, Response
from sqlalchemy.orm import session
from sqlmodel import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app import model
from ..database import get_db
from ..scemha import LoginResponse, UserLogin
from .. import utils, oauth2 , model


router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model= LoginResponse)
def login(user_credational: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(get_db)):
    
    # when we swicth to the OAuth2PasswordRequestForm   it   use   username which === email,id, name etc mean we  need to call it with username 
    
    # user = db.query(model.User).filter(model.User.email == user_credational.email).first()

    user = db.query(model.User).filter(model.User.email == user_credational.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f" Invalid Credational")
    
    
    if not utils.verify(user_credational.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail= f'invaled credationals')
    
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    return {
    "user": user,
    "token": {"access_token": access_token, "token_type": "bearer"},
}