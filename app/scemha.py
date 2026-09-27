import email
from typing import Literal, Optional
from datetime import datetime

from click import password_option
from pydantic import BaseModel, ConfigDict, EmailStr, conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class user_Response(BaseModel):
    id: int
    email: EmailStr
    # created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
                
class Post(PostBase):
    id: int
    user_id: int
    owner: user_Response
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
        
        
class userCeate(BaseModel):
    email: EmailStr
    password: str
    
    
class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]   

            
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    token: Token
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
    
class LoginResponse(BaseModel):
    user: user_Response
    token: Token
    
class Postout(BaseModel):
    Post: Post
    votes: int