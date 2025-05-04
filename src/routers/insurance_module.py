from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.insurance_module import InsuranceModuleCreate, InsuranceModuleOut, InsuranceModuleUpdate
from src.crud import insurance_module as insurance_module_crud
from src.db.session import SessionLocal

router = APIRouter(prefix="/insurance_modules", tags=["Insurance Modules"])

def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()

@router.post("/", response_model=InsuranceModuleOut)
def create_insurance_module(insurance_module: InsuranceModuleCreate, db: Session = Depends(get_db)):
    return insurance_module_crud.create_insurance_module(db, insurance_module)

@router.get("/", response_model=List[InsuranceModuleOut])
def get_insurance_modules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    insurance_modules = insurance_module_crud.get_insurance_modules(db, skip, limit)

    return insurance_modules

@router.get("/{insurance_module_id}", response_model=InsuranceModuleOut)
def get_insurance_module(insurance_module_id: str, db: Session = Depends(get_db)):
    db_insurance_module = insurance_module_crud.get_insurance_module(db, insurance_module_id)

    if db_insurance_module is None:
        raise HTTPException(status_code=404, detail="Insurance Module Not found")
    
    return db_insurance_module

@router.put("/{insurance_module_id}", response_model=InsuranceModuleOut)
def update_insurance_module(insurance_module_id: str, insurance_module: InsuranceModuleUpdate, db: Session = Depends(get_db)):
    db_insurance_module = insurance_module_crud.update_insurance_module(db, insurance_module_id, insurance_module)

    if db_insurance_module is None:
        raise HTTPException(status_code=404, detail="Insurance Module Not found")
    
    return db_insurance_module

@router.delete("/{insurance_module_id}", response_model=InsuranceModuleOut)
def delete_insurance_module(insurance_module_id: str, db: Session = Depends(get_db)):
    db_insurance_module = insurance_module_crud.delete_insurance_module(db, insurance_module_id)

    if db_insurance_module is None:
        raise HTTPException(status_code=404, detail="Insurance Module Not found")
    
    return db_insurance_module