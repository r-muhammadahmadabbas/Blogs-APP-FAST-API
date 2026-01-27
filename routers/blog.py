from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
import schemas,database,models
from sqlalchemy.orm import Session
from typing import List
from repository import blog
import oauth2


router=APIRouter(
    tags=["blog"],
    prefix="/blog"

)
@router.get("/",response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}",response_model=schemas.ShowBlog)
def show(id,db:Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)


@router.post('/',status_code=201)
def create(request:schemas.Blog,db:Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    blog.create(request,db)


@router.delete("/{id}")
def destroy(id,db:Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put("/{id}")
def update(id,request:schemas.Blog,db:Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

