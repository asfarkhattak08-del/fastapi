from xml.etree.ElementInclude import include
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from sys import exception
# import time
# import psycopg2
from psycopg2.extras import RealDictCursor # pyright: ignore[reportMissingModuleSource]
from .database import engine, Base
# from pwdlib import PasswordHash
# from sqlmodel import SQLModel, Session
# from .model import Post
# from app import model
# from .scemha import PostCreate, post_Response, user_Response, userCeate
# from random import randrange
# from turtle import update
# from typing import List, Optional
# from urllib import response
# from ast import Break, Del
# from gettext import find
# from logging import raiseExceptions
# from operator import ge
# from fastapi import Depends, FastAPI, Body , Response , status ,HTTPException


from .routers import posts,users, auth,vote

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Base.metadata.create_all(bind=engine)



    
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi', user='postgres',
#                                 password='your_new_password', cursor_factory= RealDictCursor )
#         cursor = conn.cursor()
#         print("Database connection was successfully")
#         break
        
#     except exception as error:
#         print("Connection to Database Faild")
#         print("error: ", error)
#         time.sleep(2)
    
    


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

    
    
    
# from sqlmodel import Session

# def get_db():
#     with Session(engine) as db:
#         yield db


# def find_post(id):
#     for p in my_post:
#         if p['id'] == id:
#             return p

# def find_index_post(id):
#     for i , p in enumerate(my_post):
#         if p['id'] == id:
#             return i


# @app.get("/")
# def root():
#     return{"message":"hello Asfar kahttak"} 


# @app.get("/sqlalchemy")
# def test_posts( db: Session = Depends(get_db)):
#     posts = db.query(model.Post).all()
#     return posts
    


