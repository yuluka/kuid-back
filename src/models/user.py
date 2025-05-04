import datetime
from typing import List
from sqlalchemy import Boolean, CHAR, Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from src.db.base import Base
from .associations import t_user_achievement, t_user_insurance_module, t_user_reward

# from .achievement import Achievement
# from .insurance_module import InsuranceModule
# from .reward import Reward
# from .metric import Metric
# from .notification import Notification

class USER(Base):
    __tablename__ = "USER"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="USER_pkey"),
        UniqueConstraint("email", name="user_email_un")
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(1000))
    lastname: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(100))
    cellphone: Mapped[str] = mapped_column(String(10))
    password: Mapped[str] = mapped_column(String(100))
    score: Mapped[int] = mapped_column(Integer)
    address: Mapped[str] = mapped_column(String(100))
    birth_date: Mapped[datetime.datetime] = mapped_column(DateTime)

    achievement: Mapped[List["Achievement"]] = relationship("Achievement", secondary=t_user_achievement, back_populates="user")
    insurance_module: Mapped[List["InsuranceModule"]] = relationship("InsuranceModule", secondary=t_user_insurance_module, back_populates="user")
    reward: Mapped[List["Reward"]] = relationship("Reward", secondary=t_user_reward, back_populates="user")    
    metric: Mapped[List["Metric"]] = relationship("Metric", back_populates="user")
    notification: Mapped[List["Notification"]] = relationship("Notification", back_populates="user")

    @property
    def str_id(self):
        return str(self.id)