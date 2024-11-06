from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from .database import engine
from app.routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

# Alembic migration doesn't need to do anything because it is already in database from code, in line below.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

