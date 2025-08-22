import enum
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, Integer, ForeignKey, DateTime, Text
from app.db.base_class import Base
from app.models.user import User


class AuditAction(str, enum.Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    STATUS_CHANGE = "STATUS_CHANGE"


class BrandAudit(Base):
    __tablename__ = "brand_audits"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    brand_id: Mapped[int] = mapped_column(Integer, nullable=False)
    brand_name: Mapped[str] = mapped_column(String(100), nullable=False)

    action: Mapped[AuditAction] = mapped_column(Enum(AuditAction), nullable=False)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    user_email: Mapped[str] = mapped_column(String(255), nullable=False)

    old_values: Mapped[str | None] = mapped_column(Text, nullable=True)
    new_values: Mapped[str | None] = mapped_column(Text, nullable=True)
    changes_summary: Mapped[str | None] = mapped_column(String(500), nullable=True)

    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(500), nullable=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    user: Mapped["User"] = relationship("User", back_populates="brand_audits")

    def __str__(self):
        return (
            f"{self.action} on {self.brand_name} by "
            f"{self.user_email} at {self.timestamp}"
        )
