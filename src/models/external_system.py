import datetime
from typing import List
from sqlalchemy import Boolean, DateTime, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from src.db.base import Base

# from .metric import Metric

class ExternalSystem(Base):
    __tablename__ = "external_system"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="external_system_pkey"),
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    connection_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    status: Mapped[bool] = mapped_column(Boolean)

    metric: Mapped[List["Metric"]] = relationship("Metric", back_populates="external_system")
