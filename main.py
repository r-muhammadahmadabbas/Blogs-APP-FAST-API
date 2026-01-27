from fastapi import FastAPI
import schemas,models
from database import engine
from routers import blog,user,authentication
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500", # Common Live Server port
    "*" # WARNING: Allows all origins (good for testing, restrict in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)

