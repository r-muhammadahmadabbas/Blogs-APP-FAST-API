import schemas,database,models
from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import hashing
import user_token

router=APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail={"message":"user not found"})
    if not hashing.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail={"message":"incorrect password"})
    access_token = user_token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}