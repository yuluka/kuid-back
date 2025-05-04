from typing import List
from sqlalchemy import Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

# from .user import USER

class Achievement(Base):
    __tablename__ = "achievement"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="achievement_pkey"),
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    necessary_points: Mapped[int] = mapped_column(Integer)

    user: Mapped[List["USER"]] = relationship("USER", secondary="user_achievement", back_populates="achievement")
