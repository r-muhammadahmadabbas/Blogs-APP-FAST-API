from sqlalchemy.orm import Session
import schemas
import models
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=404,detail={"message":"blog not found"})

    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return JSONResponse(status_code=204,content="deleted blog sucessfully")


def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog:
        raise HTTPException(status_code=404,detail="Not Found")
    
    blog.update(request.dict(),synchronize_session=False)

    db.commit()
    return JSONResponse(status_code=200,content={"message":"Blog Updated Sucessfully"})


def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=404,detail={"message":"blog not found"})
    return blog