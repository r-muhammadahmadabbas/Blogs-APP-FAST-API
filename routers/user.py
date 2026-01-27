from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
import schemas,database,models
from sqlalchemy.orm import Session
from typing import List
import hashing
from repository import user
get_db=database.get_db


router=APIRouter(
    tags=["Users"],
    prefix="/user"
)

@router.post("/",response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    return user.create_user(request,db)



@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)