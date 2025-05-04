from typing import List
from sqlalchemy.orm import Session
from src.models.insurance_module import InsuranceModule
from src.schemas.insurance_module import InsuranceModuleCreate, InsuranceModuleUpdate
import uuid

def create_insurance_module(db: Session, insurance_module: InsuranceModuleCreate) -> InsuranceModule:
    db_insurance_module = InsuranceModule(**insurance_module.model_dump(), id=str(uuid.uuid4())[:20])

    db.add(db_insurance_module)
    db.commit()
    db.refresh(db_insurance_module)

    return db_insurance_module

def get_insurance_modules(db: Session, skip: int = 0, limit: int = 100) -> List[InsuranceModule]:
    return db.query(InsuranceModule).offset(skip).limit(limit).all()

def get_insurance_module(db: Session, insurance_module_id: str) -> InsuranceModule:
    return db.query(InsuranceModule).filter(InsuranceModule.id == insurance_module_id).first()

def update_insurance_module(db: Session, insurance_module_id: str, insurance_module: InsuranceModuleUpdate) -> InsuranceModule:
    db_insurance_module = db.query(InsuranceModule).filter(InsuranceModule.id == insurance_module_id).first()

    if db_insurance_module:
        for key, value in insurance_module.model_dump(exclude_unset=True).items():
            setattr(db_insurance_module, key, value)

        db.commit()
        db.refresh(db_insurance_module)

        return db_insurance_module
    
def delete_insurance_module(db: Session, insurance_module_id: str) -> InsuranceModule:
    db_insurance_module = db.query(InsuranceModule).filter(InsuranceModule.id == insurance_module_id).first()

    if db_insurance_module:
        db.delete(db_insurance_module)
        db.commit()

    return db_insurance_module