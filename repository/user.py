from sqlalchemy.orm import Session
import schemas
import models
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import hashing


def create_user(request:schemas.User,db:Session):
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def show(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail={"message":"user not found"})
    return user