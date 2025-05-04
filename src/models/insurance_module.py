import datetime
from typing import List
from sqlalchemy import Integer,PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

# from .user import USER

class InsuranceModule(Base):
    __tablename__ = "insurance_module"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="insurance_module_pkey"),
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    monthly_price: Mapped[int] = mapped_column(Integer)

    user: Mapped[List["USER"]] = relationship("USER", secondary="user_insurance_module", back_populates="insurance_module")