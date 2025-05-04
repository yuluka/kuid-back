from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint, String
from sqlalchemy.orm import  Mapped, mapped_column
from src.db.base import Base

from .external_system import ExternalSystem

class Device(ExternalSystem):
    __tablename__ = "device"
    __table_args__ = (
        ForeignKeyConstraint(["id"], ["external_system.id"], name="device_id_fkey"),
        PrimaryKeyConstraint("id", name="device_pkey")
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)