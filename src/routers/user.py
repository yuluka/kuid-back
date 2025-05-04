from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.schemas.user import UserCreate, UserOut
from src.crud import user as user_crud
from src.db.session import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()

    try:
        yield db
        
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserOut:
    return user_crud.create_user(db, user)

@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[UserOut]:
    users = user_crud.get_users(db, skip=skip, limit=limit)
    
    return users

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: str, db: Session = Depends(get_db)) -> UserOut:
    db_user = user_crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@router.get("/email/{email}", response_model=UserOut)
def read_user_by_email(email: str, db: Session = Depends(get_db)) -> UserOut:
    db_user = user_crud.get_user_by_email(db, email=email)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: str, user: UserCreate, db: Session = Depends(get_db)) -> UserOut:
    db_user = user_crud.update_user(db, user_id=user_id, user=user)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: str, db: Session = Depends(get_db)) -> UserOut:
    db_user = user_crud.delete_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user