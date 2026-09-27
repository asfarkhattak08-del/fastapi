

from unittest import result

from sqlalchemy import func

from ..scemha import PostCreate, Post, Postout
from fastapi import APIRouter, Depends, status ,HTTPException,Response
from sqlmodel import  Session
from app import model
from ..database import get_db
from typing import List, Optional
from .. import oauth2
from app import scemha
# from urllib import response
# from ..scemha import  user_Response, userCeate 
# from pwdlib import PasswordHash




router = APIRouter(
    prefix= "/posts",
    tags= ['posts']
)

    
@router.get("/" , response_model= List[scemha.Postout])
# @router.get("/" )
def get_posts(db: Session = Depends(get_db),limit: int = 5, skip: int= 0, search: Optional[str] = ""):
    
    # post = db.query(model.Post).limit(limit).offset(skip).all()
    
    result = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(model.Vote,
        model.Vote.post_id == model.Post.id, isouter=True).group_by(model.Post.id).all()
    

    return [{"Post": post, "votes": votes} for post, votes in result]


@router.post("/" , response_model= Post)
def create_post(post: PostCreate, db: Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 10000)
    # my_post.append(post_dict)
    # cursor.execute(""" INSERT INTO posts (content,title,published)
    # VALUES({post.title},{post.content},{post.publish})""")  on this the attacker can Use SQL injection to mainpulate data
    
    # cursor.execute(""" INSERT INTO posts (content,title,published) VALUES(%s,%s,%s) 
    #                RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    
    # print(**post.dict())
    # new_post = model.Post(
    #     title= post.title, content= post.content, published= post.published)
    
    
    
    new_post = model.Post(user_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
     
    return new_post





# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_post[len(my_post) - 1]
#     return post



@router.get("/{id}" , response_model= Postout)
def get_post(response: Response , id: int, db: Session = Depends(get_db),user_id : str = Depends(oauth2.get_current_user)):
    # post = find_post(id)
    
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (id,))
    # post = cursor.fetchone()
    
    
    # post = db.query(model.Post).filter(model.Post.id == id).first()
    post= db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(model.Vote,
        model.Vote.post_id == model.Post.id, isouter=True).group_by(model.Post.id).filter(model.Post.id == id).first()
    
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"This the post {id} was not found ")
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return{"message": f"Post with id : {id} not found.."}
    return post


    
    

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_by_index(id: int,  db: Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user) ):

    
    # cursor.execute(""" DELETE FROM posts WHERE id = %s  RETURNING * """, (id,))
    # Delete_post = cursor.fetchone()
    # conn.commit()
    
    Delete_post = db.query(model.Post).filter(model.Post.id == id)
    post = Delete_post.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"USer Not Found for {id}")
        
    
    
    if post.user_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


    Delete_post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}")
def update_full_object(id:int, updated_post:PostCreate, db: Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
    # index = find_index_post(id)
    
    # cursor.execute("""
    #     UPDATE posts 
    #     SET title = %s, content = %s, published = %s
    #     WHERE id = %s 
    #     RETURNING *
    # """, (post.title, post.content, post.published,id))
    
    
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    
    updated_post_quary = db.query(model.Post).filter(model.Post.id == id)
    db_post = updated_post_quary.first()
    

    if db_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail= f"USer Not Found for {id}")
        
    if db_post.user_id != int(current_user.id):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f" this not your post")
    
    updated_post_quary.update(updated_post.dict(),synchronize_session= False)
    
    db.commit()
    
    
    # post_dict = post.dict()
    # post_dict["id"] = id
    # my_post[index] = post_dict
    
    return updated_post


