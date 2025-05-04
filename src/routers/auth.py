from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.user import UserLogin, UserOut
from src.crud import user as user_crud
from src.db.session import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()

    try:
        yield db
        
    finally:
        db.close()

@router.post("/login", response_model=UserOut)
def login(credentials: UserLogin, db: Session = Depends(get_db)) -> UserOut:
    db_user = user_crud.get_user_by_email(db, email=credentials.email)

    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if db_user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return db_user