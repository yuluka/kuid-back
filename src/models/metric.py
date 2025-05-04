import decimal
from sqlalchemy import ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

# from .external_system import ExternalSystem
# from .user import USER

class Metric(Base):
    __tablename__ = "metric"
    __table_args__ = (
        ForeignKeyConstraint(["external_system_id"], ["external_system.id"], name="metric_external_system_id_fkey"),
        ForeignKeyConstraint(["user_id"], ["USER.id"], name="metric_user_id_fkey"),
        PrimaryKeyConstraint("id", name="metric_pkey")
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    value: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))
    user_id: Mapped[str] = mapped_column(String(20))
    external_system_id: Mapped[str] = mapped_column(String(20))

    external_system: Mapped["ExternalSystem"] = relationship("ExternalSystem", back_populates="metric")        
    user: Mapped["USER"] = relationship("USER", back_populates="metric")