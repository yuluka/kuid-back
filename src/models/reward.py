from typing import List
from sqlalchemy import PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

# from .user import USER

class Reward(Base):
    __tablename__ = "reward"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="reward_pkey"),
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))

    user: Mapped[List["USER"]] = relationship("USER", secondary="user_reward", back_populates="reward")        
