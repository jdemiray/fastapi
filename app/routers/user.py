from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Form
from sqlalchemy.orm import Session
from app import database, schemas, models, utils
from app.database import get_db
from app.utils import create_access_token
from datetime import timedelta


router = APIRouter(
    prefix="/users",
    tags=['users']
)

# CREATE User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# GET User by ID
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404,
                            detail="User not found")
    return user

# LOGIN User
@router.post("/login")
def login(
    username: str = Form(...),  # Change parameter name to username
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.email == username).first()  # Use username to filter
    if not user or not utils.verify(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = timedelta(minutes=60)  # Token expiration time
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}


