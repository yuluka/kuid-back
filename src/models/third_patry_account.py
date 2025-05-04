from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import Base

from .external_system import ExternalSystem

class ThirdPartyAccount(ExternalSystem):
    __tablename__ = "third_party_account"
    __table_args__ = (
        ForeignKeyConstraint(["id"], ["external_system.id"], name="third_party_account_id_fkey"),
        PrimaryKeyConstraint("id", name="third_party_account_pkey")
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    provider: Mapped[str] = mapped_column(String(100))