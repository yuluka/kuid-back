from typing import Dict, List
from sqlalchemy import insert
from sqlalchemy.orm import Session
from src.models.insurance_module import InsuranceModule
from src.models.user import USER
from src.schemas.user_insurance_module import UserInsuranceModuleCreate, UserInsuranceModuleOut, UserInsuranceModuleUpdate
from src.models.associations import t_user_insurance_module

def user_has_insurance_module(db: Session, user_id: str) -> bool:
    """
    Check if a user has any insurance modules associated with them.

    :param db: Database session.
    :type db: Session
    :param user_id: User ID to check.
    :type user_id: str
    :return: True if the user has insurance modules, False otherwise.
    :rtype: bool
    """
    
    return db.query(t_user_insurance_module).filter(t_user_insurance_module.c.user_id == user_id).count() > 0

def add_user_insurance_module(db: Session, user_insurance_module: UserInsuranceModuleCreate) -> Dict[str, str]:
    """
    Associate a user with an insurance module.

    :param db: Database session
    :type db: Session
    :param user_insurance_module: UserInsuranceModuleCreate object containing user and insurance module IDs.
    :type user_insurance_module: UserInsuranceModuleCreate
    :return: A message indicating the association was created successfully.
    :rtype: Dict[str, str]
    :raises ValueError: If the user or insurance module does not exist, or if the association already exists.
    """

    user_id: str = user_insurance_module.user_id
    insurance_module_id: str = user_insurance_module.insurance_module_id
    
    user = db.query(USER).filter(USER.id == user_id).first()

    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")

    insurance_module = db.query(InsuranceModule).filter(InsuranceModule.id == insurance_module_id).first()

    if not insurance_module:
        raise ValueError(f"Insurance module with ID {insurance_module_id} does not exist.")

    # Check if the association already exists
    existing_association = db.query(t_user_insurance_module).filter(
        t_user_insurance_module.c.user_id == user_id,
        t_user_insurance_module.c.insurance_module_id == insurance_module_id
    ).first()

    if existing_association:
        raise ValueError(f"User with ID {user_id} already has insurance module with ID {insurance_module_id}.")
    
    stmt = insert(t_user_insurance_module).values(
        user_id=user_id,
        insurance_module_id=insurance_module_id,
        status=True
    )
    db.execute(stmt)
    db.commit()

    return {"message": "Association created successfully."}


def get_user_insurance_modules(db: Session, user_id: str) -> List[UserInsuranceModuleOut]:
    """
    Get all insurance modules associated with a user.

    :param db: Database session.
    :type db: Session
    :param user_id: User ID to check.
    :type user_id: str
    :return: List of insurance modules associated with the user.
    :rtype: List[UserInsuranceModuleOut]
    :raises ValueError: If the user does not exist or if there is an error retrieving the insurance modules.
    """
    
    user = db.query(USER).filter(USER.id == user_id).first()

    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")

    return db.query(InsuranceModule).join(t_user_insurance_module).filter(
        t_user_insurance_module.c.user_id == user_id
    ).all()