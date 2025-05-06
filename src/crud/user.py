from sqlalchemy.orm import Session
from src.models.user import USER
from src.schemas.user import UserCreate, UserUpdate
import uuid

def create_user(db: Session, user: UserCreate):
    db_user = USER(**user.model_dump(), id=str(uuid.uuid4())[:20], score=0)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100) -> USER:
    return db.query(USER).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: str) -> USER:
    return db.query(USER).filter(USER.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> USER:
    return db.query(USER).filter(USER.email == email).first()

def update_user(db: Session, user_id: str, user: UserUpdate) -> USER:
    db_user = db.query(USER).filter(USER.id == user_id).first()

    if db_user:
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)

    return db_user

def update_user_by_email(db: Session, email: str, user: UserUpdate) -> USER:
    """
    Update a user by email.

    This function updates the user information in the database based on the provided email.

    :param db: The database session.
    :type db: Session
    :param email: The email of the user to update.
    :type email: str
    :param user: The user information to update.
    :type user: UserUpdate
    :return: The updated user object.
    :rtype: USER
    """
    db_user = db.query(USER).filter(USER.email == email).first()

    if db_user:
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)

    return db_user

def delete_user(db: Session, user_id: str) -> USER:
    db_user = db.query(USER).filter(USER.id == user_id).first()

    if db_user:
        db.delete(db_user)
        db.commit()

    return db_user