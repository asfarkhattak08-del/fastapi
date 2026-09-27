from fastapi import APIRouter, Depends, status ,HTTPException,Response
from sqlmodel import Session
from .. import scemha, database, model, oauth2

router = APIRouter(
    prefix="/vote",
    tags=['vote']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: scemha.Vote, db: Session = Depends(database.get_db),
        current_user: int = Depends(oauth2.get_current_user)):
    
        
    post = db.query(model.Post).filter(model.Post.id == vote.post_id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with the id: {vote.post_id} was not found ")

    
    vote_quary = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id, model.Vote.user_id == current_user.id)
    found_vote = vote_quary.first()
    
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} already voted on post {vote.post_id}")
        new_vote = model.Vote(post_id = vote.post_id, user_id= current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message": "sucessfully add vote"}
    else:
        if not found_vote: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not Found")
        
        vote_quary.delete(synchronize_session=False)
        db.commit()
        
        return{"message" : "successfully delete the vote"}
        