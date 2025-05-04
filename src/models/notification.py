import datetime
from sqlalchemy import CHAR, DateTime, ForeignKeyConstraint, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

# from .user import USER

class Notification(Base):
    __tablename__ = "notification"
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["USER.id"], name="notification_user_id_fkey"),
        PrimaryKeyConstraint("id", name="notification_pkey")
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    date: Mapped[datetime.datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(CHAR(1))
    type: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[str] = mapped_column(String(20))

    user: Mapped["USER"] = relationship("USER", back_populates="notification")