from fastapi import APIRouter, Depends, status ,HTTPException
from ..scemha import  LoginResponse, user_Response, userCeate 
from pwdlib import PasswordHash
from sqlmodel import  Session
from app import model
from ..database import get_db



password_hash = PasswordHash.recommended()


router = APIRouter(
    prefix= "/users",
    tags=['users']
)


@router.post("/" , status_code=status.HTTP_201_CREATED, response_model= user_Response )
def create_user( user: userCeate,db: Session = Depends(get_db)):
    
    hashed_password = password_hash.hash(user.password)
    user.password = hashed_password
    
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    
    return new_user   



@router.get("/{id}", response_model= user_Response)
def get_user(id: int, db: Session = Depends(get_db)):
    
    user_quary = db.query(model.User).filter(model.User.id == id).first()
    
    if user_quary == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                   detail= f"USer Not Found for {id}")


    return user_quary